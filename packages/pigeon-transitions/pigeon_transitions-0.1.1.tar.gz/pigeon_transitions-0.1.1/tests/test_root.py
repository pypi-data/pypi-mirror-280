from pigeon_transitions import RootMachine
import pytest


def test_constructor(mocker):
    init = mocker.MagicMock()
    mocker.patch("pigeon_transitions.base.BaseMachine.__init__", init)

    test_machine = RootMachine(
        1,
        2,
        collect_topics=["topic1", "topic2"],
        callback_topics=["topic3", "topic4"],
        three=3,
        four=4,
    )

    assert test_machine._client is None
    assert test_machine.parent is None
    assert test_machine._collect_topics == ["topic1", "topic2"]
    assert test_machine._callback_topics == ["topic3", "topic4"]
    assert test_machine._collected == {}
    init.assert_called_with(1, 2, model="self", three=3, four=4)


def test_add_client(mocker):
    pigeon = mocker.MagicMock()
    mocker.patch("pigeon_transitions.base.Pigeon", pigeon)

    class TestMachine(RootMachine):
        pass

    test_machine = TestMachine(
        collect_topics=["topic1", "topic2"],
        callback_topics=["topic3", "topic4"],
    )
    test_machine.add_client(
        host="1.2.3.4", port=4321, username="user", password="passcode"
    )

    pigeon.assert_called_with("TestMachine", host="1.2.3.4", port=4321)
    pigeon().connect.assert_called_with(username="user", password="passcode")
    pigeon().subscribe.assert_has_calls(
        [
            mocker.call("topic1", test_machine._message_callback),
            mocker.call("topic2", test_machine._message_callback),
            mocker.call("topic3", test_machine._message_callback),
            mocker.call("topic4", test_machine._message_callback),
        ],
        any_order=True,
    )


def test_message_callback(mocker):
    callback = mocker.MagicMock()
    mocker.patch("pigeon_transitions.base.BaseMachine.message_callback", callback)
    mocker.patch("pigeon_transitions.base.setup_logging", mocker.MagicMock())

    test_machine = RootMachine(
        collect_topics=["topic1", "topic2"],
        callback_topics=["topic3", "topic4"],
    )

    test_machine._message_callback("topic1", "some_data")
    test_machine._message_callback("topic2", "some_other_data")
    test_machine._message_callback("topic3", "more_data")
    test_machine._message_callback("topic4", "even_more_data")

    assert test_machine._collected == {
        "topic1": "some_data",
        "topic2": "some_other_data",
    }
    assert test_machine.get_collected("topic1") == "some_data"
    assert test_machine.get_collected("topic2") == "some_other_data"

    with pytest.raises(AssertionError):
        test_machine.get_collected("topic3")

    callback.assert_has_calls(
        [
            mocker.call("topic3", "more_data"),
            mocker.call("topic4", "even_more_data"),
        ]
    )

    callback.side_effect = Exception("failure!")
    test_machine._message_callback("topic3", "other_data")
    test_machine._logger.warning.assert_called_with(
        "Callback for a message on topic 'topic3' with data 'other_data' resulted in an exception:\nfailure!"
    )


def test_get_current_machine(mocker):
    state_list = ["machine1", "machine2", "state"]
    test_machine = RootMachine()
    test_machine.state = test_machine.separator.join(state_list)
    test_machine._children = {
        "machine1": mocker.MagicMock(_children={"machine2": "the value"})
    }
    assert test_machine._get_current_machine() == "the value"
