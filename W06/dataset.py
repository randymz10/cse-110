# Use a try/except statements for dealing errors.

lowest_value = 9999;
country_lowest = '';
year_lowest = 0;

highest_value = 0;
country_highest = '';
year_highest = 0;

average = 0;
qty_lines = 0;
sum_values = 0;
max_life_expectancy = 0;
country_max_life = '';
min_life_expectancy = 9999;
country_min_life = '';

year_interest = int(input('Enter the year of interest: '));

with open('life-expectancy.csv') as dataset_file:
    
    for line in dataset_file:
        parts = line.split(",");
        try:
            
            life_expectancy = float(parts[3]);
            country = parts[0];
            year = int(parts[2]);

            if life_expectancy < lowest_value:
                lowest_value = life_expectancy;
                country_lowest = country;
                year_lowest = year;

            if life_expectancy > highest_value:
                highest_value = life_expectancy;
                country_highest = country;
                year_highest = year;
        
            if year_interest == year:
                sum_values +=  life_expectancy;
                qty_lines += 1;
            
            if year_interest == year and life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy;
                country_min_life = country;
            
            if year_interest == year and life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy;
                country_max_life = country;
            
        except:
            continue;

average = sum_values / qty_lines;

print(f'\nThe overall max life expectancy is: {highest_value} from {country_highest} in {year_highest}');
print(f'The overall min life expectancy is: {lowest_value} from {country_lowest} in {year_lowest}' );
print(f'\nFor the year {year_interest}:');
print(f'The average life expectancy across all countries was {average:.2f}');
print(f'The max life expectancy was in {country_max_life} with {max_life_expectancy}');
print(f'The min life expectancy was in {country_min_life} with {min_life_expectancy}');
