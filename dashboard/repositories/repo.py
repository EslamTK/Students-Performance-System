class Repo:
    def __init__(self, model):
        self._model = model

    def get_none(self):
        return self._model.objects.none()

    def get_one(self, primary_key):
        return self._model.objects.get(pk=primary_key)

    def get_all(self):
        return self._model.objects.all()

    def delete(self, primary_key):
        self._model.objects.get(pk=primary_key).delete()

    def is_exist(self, primary_key):
        return self._model.objects.filter(pk=primary_key).exists()
