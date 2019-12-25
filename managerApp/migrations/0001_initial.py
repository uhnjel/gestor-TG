# Generated by Django 2.2.7 on 2019-12-25 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PRO', 'Profesor'), ('EST', 'Estudiante'), ('EXT', 'Externo')], max_length=20)),
                ('document_id', models.IntegerField(unique=True)),
                ('first_name_1', models.CharField(max_length=100)),
                ('first_name_2', models.CharField(max_length=100, null=True)),
                ('last_name_1', models.CharField(max_length=100)),
                ('last_name_2', models.CharField(max_length=100, null=True)),
                ('ucab_mail', models.CharField(max_length=100)),
                ('personal_mail', models.CharField(max_length=100)),
                ('phone_1', models.CharField(max_length=15)),
                ('phone_2', models.CharField(max_length=15)),
                ('observations', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateTimeField(verbose_name='fecha de entrega')),
                ('title', models.CharField(max_length=200)),
                ('academic_tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_tutor_proposal', to='managerApp.Person')),
                ('company_tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_tutor_proposal', to='managerApp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ProposalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ThesisStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('nrc', models.IntegerField()),
                ('descriptors', models.CharField(max_length=50)),
                ('thematic_category', models.CharField(max_length=50)),
                ('top_date', models.DateTimeField(verbose_name='fecha tope')),
                ('company_name', models.CharField(max_length=100)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_thesis', to='managerApp.ThesisStatus')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='term_thesis', to='managerApp.Term')),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thesis_proposal', to='managerApp.Proposal')),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_proposal', to='managerApp.ProposalStatus'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='student_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_1_proposal', to='managerApp.Person'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='student_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_2_proposal', to='managerApp.Person'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='term_proposal', to='managerApp.Term'),
        ),
        migrations.CreateModel(
            name='Defense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defense_date', models.DateTimeField(verbose_name='fecha de la defensa')),
                ('jury_1_assistance_confirmation', models.BooleanField(default=False)),
                ('jury_2_assistance_confirmation', models.BooleanField(default=False)),
                ('jury_3_assistance_confirmation', models.BooleanField(default=False)),
                ('grade', models.IntegerField()),
                ('publication_mention', models.BooleanField(default=False)),
                ('honorific_mention', models.BooleanField(default=False)),
                ('corrections_delivered', models.BooleanField(default=False)),
                ('top_date_corrections', models.DateTimeField(verbose_name='fecha tope de correcciones')),
                ('grade_uploaded', models.BooleanField(default=False)),
                ('observations', models.CharField(max_length=500)),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thesis_defense', to='managerApp.Thesis')),
            ],
        ),
    ]
