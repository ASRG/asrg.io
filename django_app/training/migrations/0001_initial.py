# Generated by Django 2.2.20 on 2021-04-17 15:17

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('costs', models.CharField(max_length=6)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('AFN', 'AFN'), ('AFA', 'AFA'), ('ALL', 'ALL'), ('ALK', 'ALK'), ('DZD', 'DZD'), ('ADP', 'ADP'), ('AOK', 'AOK'), ('AON', 'AON'), ('AOR', 'AOR'), ('AOA', 'AOA'), ('ARA', 'ARA'), ('ARM', 'ARM'), ('ARP', 'ARP'), ('ARL', 'ARL'), ('ARS', 'ARS'), ('AMD', 'AMD'), ('AWG', 'AWG'), ('AUD', 'AUD'), ('ATS', 'ATS'), ('AZM', 'AZM'), ('AZN', 'AZN'), ('BSD', 'BSD'), ('BHD', 'BHD'), ('BDT', 'BDT'), ('BBD', 'BBD'), ('BYB', 'BYB'), ('BEF', 'BEF'), ('BEC', 'BEC'), ('BEL', 'BEL'), ('BZD', 'BZD'), ('BYN', 'BYN'), ('BYR', 'BYR'), ('BMD', 'BMD'), ('BTN', 'BTN'), ('BOB', 'BOB'), ('BOL', 'BOL'), ('BOV', 'BOV'), ('BOP', 'BOP'), ('BAD', 'BAD'), ('BAN', 'BAN'), ('BAM', 'BAM'), ('BWP', 'BWP'), ('BRL', 'BRL'), ('BRC', 'BRC'), ('BRZ', 'BRZ'), ('BRE', 'BRE'), ('BRR', 'BRR'), ('BRN', 'BRN'), ('BRB', 'BRB'), ('GBP', 'GBP'), ('BND', 'BND'), ('BGN', 'BGN'), ('BGL', 'BGL'), ('BGO', 'BGO'), ('BGM', 'BGM'), ('BUK', 'BUK'), ('BIF', 'BIF'), ('XOF', 'XOF'), ('XAF', 'XAF'), ('XPF', 'XPF'), ('KYD', 'KYD'), ('CLE', 'CLE'), ('CLF', 'CLF'), ('CLP', 'CLP'), ('CNX', 'CNX'), ('COP', 'COP'), ('COU', 'COU'), ('KMF', 'KMF'), ('CRC', 'CRC'), ('HRD', 'HRD'), ('CYP', 'CYP'), ('CSK', 'CSK'), ('DKK', 'DKK'), ('DJF', 'DJF'), ('DOP', 'DOP'), ('NLG', 'NLG'), ('DDM', 'DDM'), ('ECS', 'ECS'), ('ECV', 'ECV'), ('EGP', 'EGP'), ('GQE', 'GQE'), ('ERN', 'ERN'), ('EEK', 'EEK'), ('ETB', 'ETB'), ('XEU', 'XEU'), ('FKP', 'FKP'), ('FJD', 'FJD'), ('PHP', 'PHP'), ('FIM', 'FIM'), ('FRF', 'FRF'), ('XFO', 'XFO'), ('XFU', 'XFU'), ('GMD', 'GMD'), ('GEK', 'GEK'), ('GEL', 'GEL'), ('DEM', 'DEM'), ('GHS', 'GHS'), ('GHC', 'GHC'), ('GIP', 'GIP'), ('GRD', 'GRD'), ('GTQ', 'GTQ'), ('GWP', 'GWP'), ('GNF', 'GNF'), ('GNS', 'GNS'), ('GYD', 'GYD'), ('HTG', 'HTG'), ('HNL', 'HNL'), ('HKD', 'HKD'), ('HUF', 'HUF'), ('ISJ', 'ISJ'), ('INR', 'INR'), ('IDR', 'IDR'), ('IQD', 'IQD'), ('IRR', 'IRR'), ('IEP', 'IEP'), ('ILP', 'ILP'), ('ILR', 'ILR'), ('ILS', 'ILS'), ('ITL', 'ITL'), ('JMD', 'JMD'), ('JPY', 'JPY'), ('YER', 'YER'), ('JOD', 'JOD'), ('CVE', 'CVE'), ('KHR', 'KHR'), ('CAD', 'CAD'), ('QAR', 'QAR'), ('KZT', 'KZT'), ('KES', 'KES'), ('KGS', 'KGS'), ('KWD', 'KWD'), ('CDF', 'CDF'), ('HRK', 'HRK'), ('CUC', 'CUC'), ('CUP', 'CUP'), ('LAK', 'LAK'), ('LVR', 'LVR'), ('LBP', 'LBP'), ('LSL', 'LSL'), ('LVL', 'LVL'), ('LRD', 'LRD'), ('LYD', 'LYD'), ('LTL', 'LTL'), ('LTT', 'LTT'), ('LUL', 'LUL'), ('LUC', 'LUC'), ('LUF', 'LUF'), ('MOP', 'MOP'), ('MKN', 'MKN'), ('MKD', 'MKD'), ('MGF', 'MGF'), ('MWK', 'MWK'), ('MVP', 'MVP'), ('MVR', 'MVR'), ('MYR', 'MYR'), ('MGA', 'MGA'), ('MLF', 'MLF'), ('MTL', 'MTL'), ('MTP', 'MTP'), ('MAD', 'MAD'), ('MRO', 'MRO'), ('MUR', 'MUR'), ('MXN', 'MXN'), ('MXV', 'MXV'), ('MXP', 'MXP'), ('MMK', 'MMK'), ('MDC', 'MDC'), ('MDL', 'MDL'), ('MCF', 'MCF'), ('MNT', 'MNT'), ('MAF', 'MAF'), ('MZN', 'MZN'), ('MZM', 'MZM'), ('MZE', 'MZE'), ('NAD', 'NAD'), ('ANG', 'ANG'), ('NPR', 'NPR'), ('NIO', 'NIO'), ('NIC', 'NIC'), ('NZD', 'NZD'), ('NGN', 'NGN'), ('KPW', 'KPW'), ('NOK', 'NOK'), ('TWD', 'TWD'), ('UAH', 'UAH'), ('UZS', 'UZS'), ('OMR', 'OMR'), ('XCD', 'XCD'), ('PKR', 'PKR'), ('PAB', 'PAB'), ('PGK', 'PGK'), ('PYG', 'PYG'), ('PEN', 'PEN'), ('PEI', 'PEI'), ('PES', 'PES'), ('PLZ', 'PLZ'), ('PLN', 'PLN'), ('PTE', 'PTE'), ('GWE', 'GWE'), ('XRE', 'XRE'), ('RHD', 'RHD'), ('RON', 'RON'), ('ROL', 'ROL'), ('RUR', 'RUR'), ('RUB', 'RUB'), ('RWF', 'RWF'), ('SBD', 'SBD'), ('SVC', 'SVC'), ('WST', 'WST'), ('SAR', 'SAR'), ('CSD', 'CSD'), ('RSD', 'RSD'), ('SCR', 'SCR'), ('SLL', 'SLL'), ('SGD', 'SGD'), ('SHP', 'SHP'), ('SYP', 'SYP'), ('CNY', 'CNY'), ('SKK', 'SKK'), ('SIT', 'SIT'), ('SDG', 'SDG'), ('SDP', 'SDP'), ('SOS', 'SOS'), ('ZAL', 'ZAL'), ('KRH', 'KRH'), ('KRO', 'KRO'), ('SUR', 'SUR'), ('ESP', 'ESP'), ('ESA', 'ESA'), ('ESB', 'ESB'), ('LKR', 'LKR'), ('SDD', 'SDD'), ('ZAR', 'ZAR'), ('KRW', 'KRW'), ('SSP', 'SSP'), ('SRD', 'SRD'), ('SRG', 'SRG'), ('SZL', 'SZL'), ('SEK', 'SEK'), ('CHF', 'CHF'), ('STD', 'STD'), ('TJS', 'TJS'), ('TJR', 'TJR'), ('TZS', 'TZS'), ('THB', 'THB'), ('TPE', 'TPE'), ('TOP', 'TOP'), ('TTD', 'TTD'), ('CZK', 'CZK'), ('TND', 'TND'), ('TMT', 'TMT'), ('TMM', 'TMM'), ('TRY', 'TRY'), ('TRL', 'TRL'), ('USN', 'USN'), ('USS', 'USS'), ('UGS', 'UGS'), ('UGX', 'UGX'), ('UAK', 'UAK'), ('UYU', 'UYU'), ('UYP', 'UYP'), ('UYI', 'UYI'), ('VUV', 'VUV'), ('VEF', 'VEF'), ('VEB', 'VEB'), ('AED', 'AED'), ('VNN', 'VNN'), ('VND', 'VND'), ('CHE', 'CHE'), ('CHW', 'CHW'), ('YDD', 'YDD'), ('ISK', 'ISK'), ('YUN', 'YUN'), ('YUD', 'YUD'), ('YUM', 'YUM'), ('YUR', 'YUR'), ('ZRN', 'ZRN'), ('ZRZ', 'ZRZ'), ('ZMW', 'ZMW'), ('ZMK', 'ZMK'), ('ZWR', 'ZWR'), ('ZWL', 'ZWL'), ('ZWD', 'ZWD')], max_length=10)),
                ('duration', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('link', models.URLField(blank=True)),
                ('logo', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='training/logo', verbose_name='Logo')),
            ],
        ),
    ]
