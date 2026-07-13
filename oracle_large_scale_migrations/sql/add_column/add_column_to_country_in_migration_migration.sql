alter table sh.countries
add country_iso_code_3 CHAR(3)
/

UPDATE sh.countries SET country_iso_code_3 = 'USA' WHERE country_id = 52790
/
UPDATE sh.countries SET country_iso_code_3 = 'DEU' WHERE country_id = 52776
/
UPDATE sh.countries SET country_iso_code_3 = 'GBR' WHERE country_id = 52789
/
UPDATE sh.countries SET country_iso_code_3 = 'NLD' WHERE country_id = 52784
/
UPDATE sh.countries SET country_iso_code_3 = 'IRL' WHERE country_id = 52780
/
UPDATE sh.countries SET country_iso_code_3 = 'DNK' WHERE country_id = 52777
/
UPDATE sh.countries SET country_iso_code_3 = 'FRA' WHERE country_id = 52779
/
UPDATE sh.countries SET country_iso_code_3 = 'ESP' WHERE country_id = 52778
/
UPDATE sh.countries SET country_iso_code_3 = 'TUR' WHERE country_id = 52788
/
UPDATE sh.countries SET country_iso_code_3 = 'POL' WHERE country_id = 52786
/
UPDATE sh.countries SET country_iso_code_3 = 'BRA' WHERE country_id = 52775
/
UPDATE sh.countries SET country_iso_code_3 = 'ARG' WHERE country_id = 52773
/
UPDATE sh.countries SET country_iso_code_3 = 'MYS' WHERE country_id = 52783
/
UPDATE sh.countries SET country_iso_code_3 = 'JPN' WHERE country_id = 52782
/
UPDATE sh.countries SET country_iso_code_3 = 'IND' WHERE country_id = 52781
/
UPDATE sh.countries SET country_iso_code_3 = 'AUS' WHERE country_id = 52774
/
UPDATE sh.countries SET country_iso_code_3 = 'NZL' WHERE country_id = 52785
/
UPDATE sh.countries SET country_iso_code_3 = 'ZAF' WHERE country_id = 52791
/
UPDATE sh.countries SET country_iso_code_3 = 'SAU' WHERE country_id = 52787
/
UPDATE sh.countries SET country_iso_code_3 = 'CAN' WHERE country_id = 52772
/
UPDATE sh.countries SET country_iso_code_3 = 'CHN' WHERE country_id = 52771
/
UPDATE sh.countries SET country_iso_code_3 = 'SGP' WHERE country_id = 52769
/
UPDATE sh.countries SET country_iso_code_3 = 'ITA' WHERE country_id = 52770
/

UPDATE sh.countries SET country_iso_code_3 = 'TAT' WHERE country_id between 0 and 10000
/

COMMIT
/