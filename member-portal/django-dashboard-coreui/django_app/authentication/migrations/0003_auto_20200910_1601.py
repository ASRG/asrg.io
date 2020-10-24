# Generated by Django 2.1.15 on 2020-09-10 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_migrate_initial_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'permissions': []},
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('', '--Country--'), ('Afghanistan', 'AFG - Afghanistan'), ('Albania', 'ALB - Albania'), ('Algeria', 'DZA - Algeria'), ('American Samoa', 'ASM - American Samoa'), ('Andorra', 'AND - Andorra'), ('Angola', 'AGO - Angola'), ('Anguilla', 'AIA - Anguilla'), ('Antarctica', 'ATA - Antarctica'), ('Antigua and Barbuda', 'ATG - Antigua and Barbuda'), ('Argentina', 'ARG - Argentina'), ('Armenia', 'ARM - Armenia'), ('Aruba', 'ABW - Aruba'), ('Australia', 'AUS - Australia'), ('Austria', 'AUT - Austria'), ('Azerbaijan', 'AZE - Azerbaijan'), ('Bahamas (the)', 'BHS - Bahamas (the)'), ('Bahrain', 'BHR - Bahrain'), ('Bangladesh', 'BGD - Bangladesh'), ('Barbados', 'BRB - Barbados'), ('Belarus', 'BLR - Belarus'), ('Belgium', 'BEL - Belgium'), ('Belize', 'BLZ - Belize'), ('Benin', 'BEN - Benin'), ('Bermuda', 'BMU - Bermuda'), ('Bhutan', 'BTN - Bhutan'), ('Bolivia (Plurinational State of)', 'BOL - Bolivia (Plurinational State of)'), ('Bonaire, Sint Eustatius and Saba', 'BES - Bonaire, Sint Eustatius and Saba'), ('Bosnia and Herzegovina', 'BIH - Bosnia and Herzegovina'), ('Botswana', 'BWA - Botswana'), ('Bouvet Island', 'BVT - Bouvet Island'), ('Brazil', 'BRA - Brazil'), ('British Indian Ocean Territory (the)', 'IOT - British Indian Ocean Territory (the)'), ('Brunei Darussalam', 'BRN - Brunei Darussalam'), ('Bulgaria', 'BGR - Bulgaria'), ('Burkina Faso', 'BFA - Burkina Faso'), ('Burundi', 'BDI - Burundi'), ('Cabo Verde', 'CPV - Cabo Verde'), ('Cambodia', 'KHM - Cambodia'), ('Cameroon', 'CMR - Cameroon'), ('Canada', 'CAN - Canada'), ('Cayman Islands (the)', 'CYM - Cayman Islands (the)'), ('Central African Republic (the)', 'CAF - Central African Republic (the)'), ('Chad', 'TCD - Chad'), ('Chile', 'CHL - Chile'), ('China', 'CHN - China'), ('Christmas Island', 'CXR - Christmas Island'), ('Cocos (Keeling) Islands (the)', 'CCK - Cocos (Keeling) Islands (the)'), ('Colombia', 'COL - Colombia'), ('Comoros (the)', 'COM - Comoros (the)'), ('Congo (the Democratic Republic of the)', 'COD - Congo (the Democratic Republic of the)'), ('Congo (the)', 'COG - Congo (the)'), ('Cook Islands (the)', 'COK - Cook Islands (the)'), ('Costa Rica', 'CRI - Costa Rica'), ('Croatia', 'HRV - Croatia'), ('Cuba', 'CUB - Cuba'), ('Curaçao', 'CUW - Curaçao'), ('Cyprus', 'CYP - Cyprus'), ('Czechia', 'CZE - Czechia'), ('"Côte dIvoire"', 'CIV - "Côte dIvoire"'), ('Denmark', 'DNK - Denmark'), ('Djibouti', 'DJI - Djibouti'), ('Dominica', 'DMA - Dominica'), ('Dominican Republic (the)', 'DOM - Dominican Republic (the)'), ('Ecuador', 'ECU - Ecuador'), ('Egypt', 'EGY - Egypt'), ('El Salvador', 'SLV - El Salvador'), ('Equatorial Guinea', 'GNQ - Equatorial Guinea'), ('Eritrea', 'ERI - Eritrea'), ('Estonia', 'EST - Estonia'), ('Eswatini', 'SWZ - Eswatini'), ('Ethiopia', 'ETH - Ethiopia'), ('Falkland Islands (the) [Malvinas]', 'FLK - Falkland Islands (the) [Malvinas]'), ('Faroe Islands (the)', 'FRO - Faroe Islands (the)'), ('Fiji', 'FJI - Fiji'), ('Finland', 'FIN - Finland'), ('France', 'FRA - France'), ('French Guiana', 'GUF - French Guiana'), ('French Polynesia', 'PYF - French Polynesia'), ('French Southern Territories (the)', 'ATF - French Southern Territories (the)'), ('Gabon', 'GAB - Gabon'), ('Gambia (the)', 'GMB - Gambia (the)'), ('Georgia', 'GEO - Georgia'), ('Germany', 'DEU - Germany'), ('Ghana', 'GHA - Ghana'), ('Gibraltar', 'GIB - Gibraltar'), ('Greece', 'GRC - Greece'), ('Greenland', 'GRL - Greenland'), ('Grenada', 'GRD - Grenada'), ('Guadeloupe', 'GLP - Guadeloupe'), ('Guam', 'GUM - Guam'), ('Guatemala', 'GTM - Guatemala'), ('Guernsey', 'GGY - Guernsey'), ('Guinea', 'GIN - Guinea'), ('Guinea-Bissau', 'GNB - Guinea-Bissau'), ('Guyana', 'GUY - Guyana'), ('Haiti', 'HTI - Haiti'), ('Heard Island and McDonald Islands', 'HMD - Heard Island and McDonald Islands'), ('Holy See (the)', 'VAT - Holy See (the)'), ('Honduras', 'HND - Honduras'), ('Hong Kong', 'HKG - Hong Kong'), ('Hungary', 'HUN - Hungary'), ('Iceland', 'ISL - Iceland'), ('India', 'IND - India'), ('Indonesia', 'IDN - Indonesia'), ('Iran (Islamic Republic of)', 'IRN - Iran (Islamic Republic of)'), ('Iraq', 'IRQ - Iraq'), ('Ireland', 'IRL - Ireland'), ('Isle of Man', 'IMN - Isle of Man'), ('Israel', 'ISR - Israel'), ('Italy', 'ITA - Italy'), ('Jamaica', 'JAM - Jamaica'), ('Japan', 'JPN - Japan'), ('Jersey', 'JEY - Jersey'), ('Jordan', 'JOR - Jordan'), ('Kazakhstan', 'KAZ - Kazakhstan'), ('Kenya', 'KEN - Kenya'), ('Kiribati', 'KIR - Kiribati'), ('"Korea (the Democratic Peoples Republic of)"', 'PRK - "Korea (the Democratic Peoples Republic of)"'), ('Korea (the Republic of)', 'KOR - Korea (the Republic of)'), ('Kuwait', 'KWT - Kuwait'), ('Kyrgyzstan', 'KGZ - Kyrgyzstan'), ('"Lao Peoples Democratic Republic (the)"', 'LAO - "Lao Peoples Democratic Republic (the)"'), ('Latvia', 'LVA - Latvia'), ('Lebanon', 'LBN - Lebanon'), ('Lesotho', 'LSO - Lesotho'), ('Liberia', 'LBR - Liberia'), ('Libya', 'LBY - Libya'), ('Liechtenstein', 'LIE - Liechtenstein'), ('Lithuania', 'LTU - Lithuania'), ('Luxembourg', 'LUX - Luxembourg'), ('Macao', 'MAC - Macao'), ('Madagascar', 'MDG - Madagascar'), ('Malawi', 'MWI - Malawi'), ('Malaysia', 'MYS - Malaysia'), ('Maldives', 'MDV - Maldives'), ('Mali', 'MLI - Mali'), ('Malta', 'MLT - Malta'), ('Marshall Islands (the)', 'MHL - Marshall Islands (the)'), ('Martinique', 'MTQ - Martinique'), ('Mauritania', 'MRT - Mauritania'), ('Mauritius', 'MUS - Mauritius'), ('Mayotte', 'MYT - Mayotte'), ('Mexico', 'MEX - Mexico'), ('Micronesia (Federated States of)', 'FSM - Micronesia (Federated States of)'), ('Moldova (the Republic of)', 'MDA - Moldova (the Republic of)'), ('Monaco', 'MCO - Monaco'), ('Mongolia', 'MNG - Mongolia'), ('Montenegro', 'MNE - Montenegro'), ('Montserrat', 'MSR - Montserrat'), ('Morocco', 'MAR - Morocco'), ('Mozambique', 'MOZ - Mozambique'), ('Myanmar', 'MMR - Myanmar'), ('Namibia', 'NAM - Namibia'), ('Nauru', 'NRU - Nauru'), ('Nepal', 'NPL - Nepal'), ('Netherlands (the)', 'NLD - Netherlands (the)'), ('New Caledonia', 'NCL - New Caledonia'), ('New Zealand', 'NZL - New Zealand'), ('Nicaragua', 'NIC - Nicaragua'), ('Niger (the)', 'NER - Niger (the)'), ('Nigeria', 'NGA - Nigeria'), ('Niue', 'NIU - Niue'), ('Norfolk Island', 'NFK - Norfolk Island'), ('Northern Mariana Islands (the)', 'MNP - Northern Mariana Islands (the)'), ('Norway', 'NOR - Norway'), ('Oman', 'OMN - Oman'), ('Pakistan', 'PAK - Pakistan'), ('Palau', 'PLW - Palau'), ('Palestine, State of', 'PSE - Palestine, State of'), ('Panama', 'PAN - Panama'), ('Papua New Guinea', 'PNG - Papua New Guinea'), ('Paraguay', 'PRY - Paraguay'), ('Peru', 'PER - Peru'), ('Philippines (the)', 'PHL - Philippines (the)'), ('Pitcairn', 'PCN - Pitcairn'), ('Poland', 'POL - Poland'), ('Portugal', 'PRT - Portugal'), ('Puerto Rico', 'PRI - Puerto Rico'), ('Qatar', 'QAT - Qatar'), ('Republic of North Macedonia', 'MKD - Republic of North Macedonia'), ('Romania', 'ROU - Romania'), ('Russian Federation (the)', 'RUS - Russian Federation (the)'), ('Rwanda', 'RWA - Rwanda'), ('Réunion', 'REU - Réunion'), ('Saint Barthélemy', 'BLM - Saint Barthélemy'), ('Saint Helena, Ascension and Tristan da Cunha', 'SHN - Saint Helena, Ascension and Tristan da Cunha'), ('Saint Kitts and Nevis', 'KNA - Saint Kitts and Nevis'), ('Saint Lucia', 'LCA - Saint Lucia'), ('Saint Martin (French part)', 'MAF - Saint Martin (French part)'), ('Saint Pierre and Miquelon', 'SPM - Saint Pierre and Miquelon'), ('Saint Vincent and the Grenadines', 'VCT - Saint Vincent and the Grenadines'), ('Samoa', 'WSM - Samoa'), ('San Marino', 'SMR - San Marino'), ('Sao Tome and Principe', 'STP - Sao Tome and Principe'), ('Saudi Arabia', 'SAU - Saudi Arabia'), ('Senegal', 'SEN - Senegal'), ('Serbia', 'SRB - Serbia'), ('Seychelles', 'SYC - Seychelles'), ('Sierra Leone', 'SLE - Sierra Leone'), ('Singapore', 'SGP - Singapore'), ('Sint Maarten (Dutch part)', 'SXM - Sint Maarten (Dutch part)'), ('Slovakia', 'SVK - Slovakia'), ('Slovenia', 'SVN - Slovenia'), ('Solomon Islands', 'SLB - Solomon Islands'), ('Somalia', 'SOM - Somalia'), ('South Africa', 'ZAF - South Africa'), ('South Georgia and the South Sandwich Islands', 'SGS - South Georgia and the South Sandwich Islands'), ('South Sudan', 'SSD - South Sudan'), ('Spain', 'ESP - Spain'), ('Sri Lanka', 'LKA - Sri Lanka'), ('Sudan (the)', 'SDN - Sudan (the)'), ('Suriname', 'SUR - Suriname'), ('Svalbard and Jan Mayen', 'SJM - Svalbard and Jan Mayen'), ('Sweden', 'SWE - Sweden'), ('Switzerland', 'CHE - Switzerland'), ('Syrian Arab Republic', 'SYR - Syrian Arab Republic'), ('Taiwan (Province of China)', 'TWN - Taiwan (Province of China)'), ('Tajikistan', 'TJK - Tajikistan'), ('Tanzania, United Republic of', 'TZA - Tanzania, United Republic of'), ('Thailand', 'THA - Thailand'), ('Timor-Leste', 'TLS - Timor-Leste'), ('Togo', 'TGO - Togo'), ('Tokelau', 'TKL - Tokelau'), ('Tonga', 'TON - Tonga'), ('Trinidad and Tobago', 'TTO - Trinidad and Tobago'), ('Tunisia', 'TUN - Tunisia'), ('Turkey', 'TUR - Turkey'), ('Turkmenistan', 'TKM - Turkmenistan'), ('Turks and Caicos Islands (the)', 'TCA - Turks and Caicos Islands (the)'), ('Tuvalu', 'TUV - Tuvalu'), ('Uganda', 'UGA - Uganda'), ('Ukraine', 'UKR - Ukraine'), ('United Arab Emirates (the)', 'ARE - United Arab Emirates (the)'), ('United Kingdom of Great Britain and Northern Ireland (the)', 'GBR - United Kingdom of Great Britain and Northern Ireland (the)'), ('United States Minor Outlying Islands (the)', 'UMI - United States Minor Outlying Islands (the)'), ('United States of America (the)', 'USA - United States of America (the)'), ('Uruguay', 'URY - Uruguay'), ('Uzbekistan', 'UZB - Uzbekistan'), ('Vanuatu', 'VUT - Vanuatu'), ('Venezuela (Bolivarian Republic of)', 'VEN - Venezuela (Bolivarian Republic of)'), ('Viet Nam', 'VNM - Viet Nam'), ('Virgin Islands (British)', 'VGB - Virgin Islands (British)'), ('Virgin Islands (U.S.)', 'VIR - Virgin Islands (U.S.)'), ('Wallis and Futuna', 'WLF - Wallis and Futuna'), ('Western Sahara', 'ESH - Western Sahara'), ('Yemen', 'YEM - Yemen'), ('Zambia', 'ZMB - Zambia'), ('Zimbabwe', 'ZWE - Zimbabwe'), ('Åland Islands', 'ALA - Åland Islands')], default=('', '--Country--'), max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('', 'Gender'), ('Male', 'Male'), ('Female', 'Female'), ('Prefer Not To Say', 'Prefer Not to Say')], default=('', 'Gender'), max_length=25),
        ),
        migrations.AddField(
            model_name='user',
            name='occupational_status',
            field=models.CharField(choices=[('', 'Occupational Status'), ('student', 'Student'), ('undergraduate student', 'Undergraduate Student'), ('graduate student', 'Graduate Student'), ('professional', 'Professional')], default=('', 'Occupational Status'), max_length=50),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='foundation',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='location',
            field=models.CharField(max_length=56),
        ),
        migrations.AlterField(
            model_name='user',
            name='chapter',
            field=models.ManyToManyField(related_name='users', to='authentication.Chapter'),
        ),
    ]