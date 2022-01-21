# wordle-search
A python package for calculating best starting words in Wordle

When playing the popular game [Wordle](https://www.powerlanguage.co.uk/wordle/), what is the best starting word?

# Example

Follow along in this [Google Colab notebook](https://colab.research.google.com/drive/1jhCIPP9IwM36St6mIW5nyK2uCJN3blH9?usp=sharing)

Takes a list of strings, e.g. [the 10,000 most common English words](https://github.com/first20hours/google-10000-english)

<img width="347" alt="Screen Shot 2022-01-20 at 16 24 46" src="https://user-images.githubusercontent.com/38541020/150443776-69806b1f-657a-4d81-bccd-d57f854fd77d.png">

... and searches for the most effective Wordle starting words

<img width="673" alt="Screen Shot 2022-01-20 at 16 27 57" src="https://user-images.githubusercontent.com/38541020/150443820-9b623ece-cf91-4b81-948d-aac263ddd505.png">

Or test your own strings!

<img width="620" alt="Screen Shot 2022-01-20 at 16 41 00" src="https://user-images.githubusercontent.com/38541020/150444841-d9ea3403-cc39-49cd-ab14-9aa77f6092c8.png">

## Options

Current options for "best starting word" include:
- Maximising the most likely (modal) score with lexicographic ordering, `comp_type='modal'`
- Maximising green + orange score, `comp_type='mean'` or `comp_type='sum'`
- Maximising green score, `comp_type='max_green'`
- Maximising orange score, `comp_type='max_orange'`
