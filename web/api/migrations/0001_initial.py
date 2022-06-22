# Generated by Django 4.0.5 on 2022-06-13 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuildModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild_id', models.BigIntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'guilds',
                'db_table': 'guilds',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discord_id', models.BigIntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='SavedMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('hidden', models.BooleanField(blank=True, default=False, null=True)),
                ('discord_id', models.ForeignKey(db_column='discord_id', on_delete=django.db.models.deletion.CASCADE, to='api.usermodel', to_field='discord_id')),
            ],
            options={
                'verbose_name_plural': 'saved_messages',
                'db_table': 'saved_messages',
            },
        ),
        migrations.CreateModel(
            name='InfractorSettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infractor_is_enabled', models.BooleanField(blank=True, default=False, null=True)),
                ('bad_words_is_enabled', models.BooleanField(blank=True, default=False, null=True)),
                ('bad_words_dictionary', models.TextField(blank=True, null=True)),
                ('link_filter_is_enabled', models.BooleanField(blank=True, default=False, null=True)),
                ('link_filter_dictionary', models.TextField(blank=True, null=True)),
                ('spam_detector_is_enabled', models.BooleanField(blank=True, default=False, null=True)),
                ('guild_id', models.ForeignKey(db_column='guild_id', on_delete=django.db.models.deletion.CASCADE, to='api.guildmodel', to_field='guild_id')),
            ],
            options={
                'verbose_name_plural': 'infractor_settings',
                'db_table': 'infractor_settings',
            },
        ),
    ]