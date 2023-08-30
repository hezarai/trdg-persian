from trdg.generators import GeneratorFromDict
from tqdm import tqdm


FA_ALPHABET = ' اآبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
FA_EXTRAS = 'ءؤئأّ'
FA_DIGITS = '۰۱۲۳۴۵۶۷۸۹'
EN_DIGITS = '0123456789'
EN_SYMBOLS = '!@#$%^&*()_+|/<>:;,.'
ALL = FA_ALPHABET + FA_EXTRAS + FA_DIGITS
count = 1000000
group = '2'
# The generators use the same arguments as the CLI, only as parameters

generator = GeneratorFromDict(language='fa2',
                              count=count,
                              blur=True,
                              random_blur=1,
                              word_split=True,
                              background_type=2,
                              margins=(3, 3, 3, 3),
                              fit=True
                              )

print('\n')
pbar = tqdm(generator, total=count, desc=f'Generating Images ...',
            bar_format='{desc:<10}{percentage:3.0f}%|{bar:70}{r_bar}',
            position=0, leave=True, unit='image',
            ascii=" #")


def validate_word(word):
    for c in word:
        if c not in ALL:
            return False
    return True


for i, (img, lbl) in enumerate(pbar):
    if not validate_word(lbl):
        continue
    try:
        img.save(f'./results/{group}/{i}_{lbl}.jpg')
    except:
        continue

print('\n')
