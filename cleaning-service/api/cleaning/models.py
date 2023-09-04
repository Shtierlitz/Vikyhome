# api/cleaning/models.py

from django.db import models
import cloudinary.api


class ServiceQuerySet(models.QuerySet):
    def delete(self):
        for obj in self:
            print("ServiceQuerySet delete called")
            cloudinary.api.delete_resources(obj.image, resource_type="image", type="upload")
        super().delete()


class ServiceManager(models.Manager):
    def get_queryset(self):
        return ServiceQuerySet(self.model, using=self._db)


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва послуги')
    description = models.TextField(blank=True, verbose_name="Описання послуги")
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, verbose_name="Цiна послуги")
    price_description = models.CharField(max_length=20, blank=True, verbose_name='Префiкс цiни')
    image = models.ImageField(upload_to="media/Vikyhome", verbose_name="Титульна картинка", blank=True)

    # image_public_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            # получаем старую запись из базы данных
            obj = Service.objects.get(id=self.id)

            # если картинки нету, то бросаем исклоючение и сохраняем обычным способом
            try:
                bool(obj.image.url)
            except ValueError:
                raise Service.DoesNotExist()
            # если поле icon_image было обновлено
            if obj.image != self.image:
                # удалить старое изображение с Cloudinary
                cloudinary.api.delete_resources(obj.image, resource_type="image",
                                                type="upload")
        except Service.DoesNotExist:
            # если объекта не существует, то это новый объект,
            # поэтому пропустите удаление
            pass

        super().save(*args, **kwargs)

    objects = ServiceManager()  # удаление картинки и из cloudinary


class Extra(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва додаткової послуги')
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, verbose_name="Цiна додаткової послуги")
    price_description = models.CharField(max_length=20, blank=True, verbose_name='Префiкс цiни')

    class Meta:
        verbose_name = "Додаткова послуга"
        verbose_name_plural = "Додатковi послуги"

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва посту')
    text = models.TextField(verbose_name='Вмiст тексту поста')

    class Meta:
        verbose_name = "Коментарiй"
        verbose_name_plural = "Коментарi"

    def __str__(self):
        return self.title
