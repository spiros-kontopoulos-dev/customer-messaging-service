from app.service import respond_to_message


def test_usual_order_for_repeat_customer(db):
    response = respond_to_message(
        db,
        store_id=1,
        phone="+15550001111",
        message="my usual",
    )

    assert response.store_name == "Downtown"
    assert response.suggested_item == "Margherita Pizza"
    assert response.source_order_id == 1


def test_unknown_customer_gets_non_personalized_reply(db):
    response = respond_to_message(
        db,
        store_id=1,
        phone="+15559999999",
        message="my usual",
    )

    assert response.suggested_item is None
    assert "don't recognize" in response.reply


def test_unrelated_message_does_not_lookup_usual(db):
    response = respond_to_message(
        db,
        store_id=1,
        phone="+15550001111",
        message="what time do you close?",
    )

    assert response.suggested_item is None
    assert "usual" in response.reply
