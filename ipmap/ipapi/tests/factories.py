import factory


class IPCoordFactory(factory.DjangoModelFactory):
    class Meta:
        model = "ipapi.IPCoord"

    latitude = factory.Faker("pydecimal", min_value=-90, max_value=90, right_digits=6)
    longitude = factory.Faker(
        "pydecimal", min_value=-180, max_value=180, right_digits=6
    )
    count = factory.Faker("pyint", min_value=0)
