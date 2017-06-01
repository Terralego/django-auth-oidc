from django.contrib.auth import get_user_model


def get_user_by_username(id):
	User = auth.get_user_model()
	user, created = User.objects.get_or_create(username=id["sub"])
	return user
