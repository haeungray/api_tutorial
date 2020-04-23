class Message(Resource):
    def abort_if_message_doesnt_exist(self, id):
        if id not in message_manager.messages:
            abort(status.HTTP_404_FOUND, message="Message {0} doesn't exist".format(id))


@marshal_with(message_fields)
def get(self, id):
    self.abort_if_message_doesnt_exist(id)
    return message_manager.get_message(id)

def delete(self, id):
    self.abort_if_message_doesnt_exist(id)
    message_manager.delete_message(id)
    return '', status.HTTP_204_NO_CONTENT

@marshal_with(message_fields)
def patch(self, id):
    self.abort_if_message_doesnt_exist(id)
    message = message_manager.get_message(id)
    parser = reqparse.RequestParser()
    parser.add_argument('message', type = str)
    parser.add_argument('duration', type = int)
    parser.add_argument('printed_times',type=int)
    parser.add_argument('printed_once',type = bool)
    args = parser.parse_args()
    if 'message' in args : 
        message.message = args['message']
    if 'duration' in args : 
        message.message = args['duration']
    return message