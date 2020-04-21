class Message(Resource):
    def abort_if_message_doesnt_exist(self,id):
        if id not in message_manager.messages:
            abort(status.HTTP_NOT_FOUND,
            message = 'Message {0} doesn't exist.format(id))

    @marshar_with(message_fields)
    def get(self, id):
        self.abort_if_message_doesnt_exist(id)
        return message_manager.get_message(id)