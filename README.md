# Poetry API

## Data Source - [PoetryDB](https://github.com/thundercomb/poetrydb)

## Introduction

This is an API for educational purposes. My own educational purposes.

This API is designed to respond to get requests at various endpoints to recieve either specific or random poems.

## API Reference

### Poems

<b>General Format:</b>

```
/poems[/<author>]
```

Format:

```
/poems
```

Description:
Returns all poems

Example:

```
/poems
```

Result:

```
[
  {
"author": "Emily Dickinson",
"id": 1,
"linecount": "4",
"lines": [
"Not at Home to Callers",
"Says the Naked Tree --",
"Bonnet due in April --",
"Wishing you Good Day --"
],
"title": "Not at Home to Callers"
},
...
{
"author": "Emily Dickinson",
"id": 361,
"linecount": "16",
"lines": [
"He told a homely tale",
"And spotted it with tears --",
"Upon his infant face was set",
"The Cicatrice of years --",
"",
"All crumpled was the cheek",
"No other kiss had known",
"Than flake of snow, divided with",
"The Redbreast of the Barn --",
"",
"If Mother -- in the Grave --",
"Or Father -- on the Sea --",
"Or Father in the Firmament --",
"Or Brethren, had he --",
"",
"If Commonwealth below,",
"Or Commonwealth above",
"Have missed a Barefoot Citizen --",
"I've ransomed it -- alive --"
],
"title": "He told a homely tale"
}
]
```

Format:

```
/poems/<author>
```

Description:
Returns all poems by the author, case sensitively

Example:

```
/poems/Emily Dickinson
```

Result:

```
[
  {
"author": "Emily Dickinson",
"id": 1,
"linecount": "4",
"lines": [
"Not at Home to Callers",
"Says the Naked Tree --",
"Bonnet due in April --",
"Wishing you Good Day --"
],
"title": "Not at Home to Callers"
},
...
{
"author": "Emily Dickinson",
"id": 361,
"linecount": "16",
"lines": [
"He told a homely tale",
"And spotted it with tears --",
"Upon his infant face was set",
"The Cicatrice of years --",
"",
"All crumpled was the cheek",
"No other kiss had known",
"Than flake of snow, divided with",
"The Redbreast of the Barn --",
"",
"If Mother -- in the Grave --",
"Or Father -- on the Sea --",
"Or Father in the Firmament --",
"Or Brethren, had he --",
"",
"If Commonwealth below,",
"Or Commonwealth above",
"Have missed a Barefoot Citizen --",
"I've ransomed it -- alive --"
],
"title": "He told a homely tale"
}
]
```

### Title

<b>General Format:</b>

```
/title[/<title>]
```

Format:

```
/title
```

Description:
Returns a random poem's title

Example:

```
/title
```

Result:

```
"I lost a World -- the other day!"
```

Format:

```
/title/<title>
```

Descrition:
Returns all poems with `<title>` in the title

Example:

```
/title/spring
```

Result:

```
[
{
"author": "Emily Dickinson",
"id": 5,
"linecount": "8",
"lines": [
"The Notice that is called the Spring",
"Is but a month from here --",
"Put up my Heart thy Hoary work",
"And take a Rosy Chair.",
"",
"Not any House the Flowers keep --",
"The Birds enamor Care --",
"Our salary the longest Day",
"Is nothing but a Bier."
],
"title": "The Notice that is called the Spring"
},
...
{
"author": "Emily Dickinson",
"id": 319,
"linecount": "8",
"lines": [
"Spring is the Period",
"Express from God.",
"Among the other seasons",
"Himself abide,",
"",
"But during March and April",
"None stir abroad",
"Without a cordial interview",
"With God."
],
"title": "Spring is the Period"
}
]
```

### Random

<b>General Format:</b>

```
/random[/<author>]
```

Format:

```
/random
```

Description:
Returns a random poem

Example:

```
/random
```

Result:

```
{
"author": "Algernon Charles Swinburne",
"id": 398,
"linecount": "30",
"lines": [
"ALL the bells of heaven may ring,",
"All the birds of heaven may sing,",
"All the wells on earth may spring,",
"All the winds on earth may bring",
"All sweet sounds together---",
"Sweeter far than all things heard,",
"Hand of harper, tone of bird,",
"Sound of woods at sundawn stirred,",
"Welling water's winsome word,",
"Wind in warm wan weather,",
"",
"One thing yet there is, that none",
"Hearing ere its chime be done",
"Knows not well the sweetest one",
"Heard of man beneath the sun,",
"Hoped in heaven hereafter;",
"Soft and strong and loud and light,",
"Very sound of very light",
"Heard from morning's rosiest height,",
"When the soul of all delight",
"Fills a child's clear laughter.",
"",
"Golden bells of welcome rolled",
"Never forth such notes, nor told",
"Hours so blithe in tones so bold,",
"As the radiant mouth of gold",
"Here that rings forth heaven.",
"If the golden-crested wren",
"Were a nightingale---why, then,",
"Something seen and heard of men",
"Might be half as sweet as when",
"Laughs a child of seven."
],
"title": "A Child's Laughter"
}
```

Format:

```
/random/<author>
```

Example:

```
/random/Algernon Charles Swinburne
```

Result:

```
{
"author": "Algernon Charles Swinburne",
"id": 391,
"linecount": "11",
"lines": [
"Birth and death, twin-sister and twin-brother,",
"Night and day, on all things that draw breath,",
"Reign, while time keeps friends with one another",
"Birth and death.",
"",
"Each brow-bound with flowers diverse of wreath,",
"Heaven they hail as father, earth as mother,",
"Faithful found above them and beneath.",
"",
"Smiles may lighten tears, and tears may smother",
"Smiles, for all that joy or sorrow saith:",
"Joy nor sorrow knows not from each other",
"Birth and death."
],
"title": "Birth And Death"
}
```

### Lines

<b>General Format:</b>

```
/lines
```

Format:

```
/lines
```

Description:
Returns a random line from a random poem

Example:

```
/lines
```

Result:

```
"But since it is playing -- kill us,"
```

## License

To protect the openness of this endeavour the software is released under the terms of the [GNU Public License v2](https://github.com/thundercomb/poetrydb/blob/master/LICENSE.txt). In essence it allows you to reuse and modify this software, as long as the resulting program(s) remain open and licensed in the same way.

```

```
