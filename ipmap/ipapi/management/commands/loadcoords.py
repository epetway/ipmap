import csv
from collections import defaultdict
from decimal import Decimal
from io import BytesIO, TextIOWrapper
from zipfile import ZipFile

import requests
from tqdm import tqdm

from django.core.management.base import BaseCommand, CommandError

from ipapi.models import IPCoord


class Command(BaseCommand):
    help = "Load GeoLite IP address data"

    def load_data(self, csvfile):
        row_count = 0
        self.stdout.write("Loading file...")
        response = requests.get(
            "https://ipmapfiles.s3.amazonaws.com/GeoLite2-City-Blocks-IPv4.zip"
        )

        with ZipFile(BytesIO(response.content)) as zf:
            with zf.open("GeoLite2-City-Blocks-IPv4.csv", "r") as infile:
                reader = csv.DictReader(TextIOWrapper(infile, "utf-8"))
                # TODO: might be nice to have rotating progress marker here
                # REVIEW: I know it adds a bit of processing time to get the
                # row count, but it is nice to have a total progress bar later
                # for the actual file processing.
                row_count = 0
                self.stdout.write("Getting row count...")
                for row in reader:
                    row_count += 1
                infile.seek(0)
                coord_counts = defaultdict(int)
                next(reader)
                for row in tqdm(
                    reader, total=row_count, desc="Processing file...", unit="rows "
                ):
                    if row["latitude"] == "" or row["longitude"] == "":
                        continue
                    coord_counts[(row["latitude"], row["longitude"])] += 1
                ipcoords = []
                for coord, count in tqdm(
                    coord_counts.items(),
                    total=len(coord_counts),
                    desc="Creating model instances to be bulk loaded...",
                ):
                    ipcoords.append(
                        IPCoord(
                            latitude=Decimal(coord[0]),
                            longitude=Decimal(coord[1]),
                            count=count,
                        )
                    )
        IPCoord.objects.all().delete()
        self.stdout.write("Sending objects to database...")
        IPCoord.objects.bulk_create(ipcoords, batch_size=1000)
        self.stdout.write(
            self.style.SUCCESS(f"Created {len(coord_counts)} coordinates.")
        )
        self.stdout.write(self.style.SUCCESS("Done!"))

    def handle(self, *args, **options):
        self.load_data(options.get("csvfile"))
