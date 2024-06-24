import pytest
import scalify
from pydantic import BaseModel, Field
from scalify.utilities.testing import assert_locations_equal


class Location(BaseModel):
    city: str
    state: str = Field(description="The two letter abbreviation")


@pytest.fixture(autouse=True)
def use_gpt4o_for_all_tests(gpt_4):
    pass


@pytest.mark.flaky(max_runs=3)
class TestVisionCast:
    def test_cast_ny(self):
        img = scalify.Image(
            "https://images.unsplash.com/photo-1568515387631-8b650bbcdb90"
        )
        result = scalify.cast(img, target=Location)
        assert_locations_equal(result, Location(city="New York", state="NY"))

    def test_cast_dc(self):
        img = scalify.Image(
            "https://images.unsplash.com/photo-1617581629397-a72507c3de9e"
        )
        result = scalify.cast(img, target=Location)
        assert isinstance(result, Location)
        assert_locations_equal(result, Location(city="Washington", state="DC"))

    def test_cast_ny_image_and_text(self):
        img = scalify.Image(
            "https://images.unsplash.com/photo-1568515387631-8b650bbcdb90"
        )
        result = scalify.cast(
            data=["I see a tall building", img],
            target=Location,
        )
        assert_locations_equal(result, Location(city="New York", state="NY"))

    def test_cast_book(self):
        class Book(BaseModel):
            title: str
            subtitle: str
            authors: list[str]

        img = scalify.Image("https://hastie.su.domains/ElemStatLearn/CoverII_small.jpg")
        result = scalify.cast(img, target=Book)
        assert result == Book(
            title="The Elements of Statistical Learning",
            subtitle="Data Mining, Inference, and Prediction",
            authors=["Trevor Hastie", "Robert Tibshirani", "Jerome Friedman"],
        )


class TestAsync:
    async def test_cast_ny(self):
        img = scalify.Image(
            "https://images.unsplash.com/photo-1568515387631-8b650bbcdb90"
        )
        result = await scalify.cast_async(img, target=Location)
        assert_locations_equal(result, Location(city="New York", state="NY"))


class TestMapping:
    def test_map(self):
        ny = scalify.Image(
            "https://images.unsplash.com/photo-1568515387631-8b650bbcdb90"
        )
        dc = scalify.Image(
            "https://images.unsplash.com/photo-1617581629397-a72507c3de9e"
        )
        result = scalify.cast.map([ny, dc], target=Location)
        assert isinstance(result, list)
        assert_locations_equal(result[0], Location(city="New York", state="NY"))
        assert_locations_equal(result[1], Location(city="Washington", state="DC"))

    @pytest.mark.flaky(max_runs=2)
    async def test_async_map(self):
        ny = scalify.Image(
            "https://images.unsplash.com/photo-1568515387631-8b650bbcdb90"
        )
        dc = scalify.Image(
            "https://images.unsplash.com/photo-1617581629397-a72507c3de9e"
        )
        result = await scalify.cast_async.map([ny, dc], target=Location)
        assert isinstance(result, list)

        assert_locations_equal(result[0], Location(city="New York", state="NY"))
        assert_locations_equal(result[1], Location(city="Washington", state="DC"))
