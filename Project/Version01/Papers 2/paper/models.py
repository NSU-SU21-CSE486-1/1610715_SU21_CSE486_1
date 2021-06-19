from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    contract_no = models.IntegerField()
    email_id = models.CharField(max_length=250)
    team_id = models.IntegerField()

    def __str__(self):
        return self.first_name

class Projects(models.Model):
    project_id =  models.ForeignKey(Users, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name

class Teams(models.Model):
    team_id = models.ForeignKey(Projects, on_delete=models.CASCADE) 
    team_members = models.CharField(max_length=200)
    

    def __str__(self):
        return self.team_id

class Document_Folder(models.Model):
    folder_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    folder_type = models.CharField(max_length=20)
    

    def __str__(self):
        return self.folder_type

class Document_File(models.Model):
    file_id = models.ForeignKey(Document_Folder, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=20)
    file_name = models.CharField(max_length=200)

    def __str__(self):
        return self.file_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)