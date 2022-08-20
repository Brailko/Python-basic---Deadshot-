import pytest
from main import *

def test_add_message():
	user1 = User("Boris")
	user2 = User("Roman")
	user1.add_message('test_message_incoming')
	user1.add_message('test_message_outgoing', False)
	assert user1.incoming_messages == ['test_message_incoming']
	assert user1.outgoing_messages == ['test_message_outgoing']


def test_get_last_message():
	user1 = User("Boris")
	user1.incoming_messages = ['test_message_1', 'test_message_2']
	assert user1.get_last_message() == 'test_message_2'


@pytest.mark.parametrize('attribut1, attribut2, all_messages',
						 [(True, True, {'incomings': ['test_message_incoming_1'],  'outgoings': ['test_message_outgoing_1']} ),
						  (True, False, {'incomings': ['test_message_incoming_1'], 'outgoings': None}),
						  (False, True, {'incomings': None, 'outgoings': ['test_message_outgoing_1']}),
						  (False, False, {'incomings': None, 'outgoings': None})])
def test_get_all_messages(attribut1, attribut2, all_messages):
	user1 = User("Boris")
	user1.incoming_messages = ['test_message_incoming_1']
	user1.outgoing_messages = ['test_message_outgoing_1']
	assert  user1.get_all_messages(attribut1, attribut2) == all_messages


def test_read_last_message():
	user1 = User("Boris")
	user1.incoming_messages = ['test_message_incoming_1', 'test_message_incoming_2']
	assert user1.read_last_message() == 'test_message_incoming_2'
	assert user1.incoming_messages == ['test_message_incoming_1']


def test_read_all_messages():
	user1 = User("Boris")
	user1.incoming_messages = ['test_message_incoming_1', 'test_message_incoming_2']
	assert user1.read_all_messages() == ['test_message_incoming_1', 'test_message_incoming_2']
	assert user1.incoming_messages == []


def test_get_message_by_id():
	user1 = User("Boris")
	user1.incoming_messages = ['test_message_incoming_1', 'test_message_incoming_2']
	assert user1.get_message_by_id(1) == 'test_message_incoming_2'


def test_edit_message():
	user1 = User("Boris")
	user2 = User("Roman")
	test_message = Message(user1, user2, datetime.now(), "Hi my friend")
	test_message.edit('Hi. How are you?')
	assert test_message.text == 'Hi. How are you?'


if __name__ == '__main__':
	pytest.main()