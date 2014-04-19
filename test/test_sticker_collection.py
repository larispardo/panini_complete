from nose import with_setup
from Panini import StickerCollection
from Panini import Pack
from unittest.mock import Mock
import Panini

def setup_add_pack():
    Pack.generate_pack = Mock(return_value = [1])
    global new_collection
    new_collection = StickerCollection.StickerCollection(Panini.NUMBER_OF_STICKERS, Panini.STICKERS_TO_REQUEST, Panini.STICKERS_PER_PACK)
    new_collection.add_pack()

@with_setup(setup_add_pack)
def test_add_pack_increases_the_sticker_count_if_a_new_sticker_is_added():
    assert new_collection.stickers == 1, "add_pack doesn't add to the sticker count"

@with_setup(setup_add_pack)
def test_add_pack_adds_a_sticker_to_the_collection():
    assert new_collection.collection[1] == 1, "add_pack doesn't add the sticker to the collection"

def test_packs_until_complete_returns_packs_till_stickers_minus_threshold_reached():
    complete_collection = StickerCollection.StickerCollection(10, 5, 1)
    Pack.generate_pack = Mock(side_effect = [[1],[2], [3], [4], [5]])
    total_packs = complete_collection.packs_till_complete()
    assert total_packs == 5, "packs_till_complete was {0}".format(total_packs)
