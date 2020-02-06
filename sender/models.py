from django.db import models
from django.core.mail import send_mail
import threading
import time

# Create your models here.
class MailForSend(models.Model):
    mailer = models.EmailField(help_text="Введите Email получателя")
    subject = models.CharField(max_length=50, help_text="Тема письма, не более 50 знаков.")
    text = models.TextField()
    sec_to_send = models.BigIntegerField()
    is_send = models.BooleanField(default=False)
        
    def save(self, *args, **kwargs):
        if not self.is_send:
            
            super(MailForSend, self).save(*args, **kwargs) # Выполнение настоящего save().
            
            def send_maile_with_delay(mailer, subject, text, sec_to_send, *args, **kwargs):
                #print('Utils. Задача ', subject, ' получена в: ', time.ctime())
                time.sleep(sec_to_send)
                #print('Utils. Задача ', subject, ' выполнена в: ', time.ctime())
                send_mail(subject, text, 'umqambi@yandex.by', [mailer], fail_silently=False,)
                self.is_send = True
                #print('тема во вложенной ', self.subject)
                super(MailForSend, self).save(update_fields=['is_send'])

            t = threading.Thread(
                target=send_maile_with_delay, 
                args=(self.mailer, self.subject, self.text, self.sec_to_send, self)
            )
            t.daemon = True
            t.start()
        else:
            print('тема ', self.subject, 'is_send = ', self.is_send)



