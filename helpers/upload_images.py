def upload_movie_image(instance, filename):
    return f"{instance.title}/{filename}"


def upload_actor_image(instance, filename):
    return f"{instance.first_name}_{instance.last_name}/{filename}"
