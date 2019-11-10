import csv
from collections import defaultdict
from decimal import Decimal

from tqdm import tqdm

from django.core.management.base import BaseCommand, CommandError

from ipapi.models import IPCoord


class Command(BaseCommand):
    help = "Load GeoLite IP address data"

    def add_arguments(self, parser):
        parser.add_argument("csvfile", type=str, help="GeoLite csv file")

    def load_data(self, csvfile):
        row_count = 0
        self.stdout.write("Loading file...")
        with open(csvfile, "r") as infile:
            reader = csv.DictReader(infile)
            row_count = 0
            # TODO: might be nice to have rotating progress marker here
            # REVIEW: I know it adds a bit of processing time to get the
            # row count, but it is nice to have a total progress bar later
            # for the actual file processing.
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
            created_count = 0
            updated_count = 0
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
            self.stdout.write("Sending objects to database...")
            IPCoord.objects.bulk_create(ipcoords, batch_size=1000)
        if created_count:
            self.stdout.write(
                self.style.SUCCESS(f"Created {created_count} coordinates.")
            )
        if updated_count:
            self.stdout.write(
                self.style.SUCCESS(f"Updated {updated_count} coordinates.")
            )
        self.stdout.write(self.style.SUCCESS("All Done!"))

    def handle(self, *args, **options):
        self.load_data(options.get("csvfile"))
