from math import floor

cat_species = input()
cat_sex = input()
mounts_cat_life = 0
real_cat = True

if cat_species == 'British Shorthair':
    if cat_sex == 'm':
        years_of_life = 13
        mounts_cat_life = years_of_life * 12 / 6
    else:
        years_of_life = 14
        mounts_cat_life = years_of_life * 12 / 6

elif cat_species == 'Siamese':
    if cat_sex == 'm':
        years_of_life = 15
        mounts_cat_life = years_of_life * 12 / 6
    else:
        years_of_life = 16
        mounts_cat_life = years_of_life * 12 / 6

elif cat_species == 'Persian':
    if cat_sex == 'm':
        years_of_life = 14
        mounts_cat_life = years_of_life * 12 / 6
    else:
        years_of_life = 15
        mounts_cat_life = years_of_life * 12 / 6

elif cat_species == 'Ragdoll':
    if cat_sex == 'm':
        years_of_life = 16
        mounts_cat_life = years_of_life * 12 / 6
    else:
        years_of_life = 17
        mounts_cat_life = years_of_life * 12 / 6

elif cat_species == 'American Shorthair':
    if cat_sex == 'm':
        years_of_life = 12
        mounts_cat_life = years_of_life * 12 / 6
    else:
        years_of_life = 13
        mounts_cat_life = years_of_life * 12 / 6

elif cat_species == 'Siberian':
    if cat_sex == 'm':
        years_of_life = 11
        mounts_cat_life = years_of_life * 12 / 6
    else:
        years_of_life = 12
        mounts_cat_life = years_of_life * 12 / 6

else:
    real_cat = False

if real_cat:
    print(f"{floor(mounts_cat_life)} cat months")
else:
    print(f'{cat_species} is invalid cat!')
