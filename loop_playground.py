data = [
  {
    'list': [1,2,3],
    'dict': {'a':'aardvark', 'b':'banana'},
    "hashtags":[
      {"indices":[32,36],"text":"lol"},
      {"indices":[32,36],"text":"yummy"}
    ]
  }, 
  {
    'list': [10,20,30],
    'dict': {'a':'apple', 'b':'breakfast'},
    "hashtags":[
      {"indices":[32,36],"text":"lol"}
    ]
  }, 
  {
    'list': [100,200,300],
    'dict': {'a':'avocado', 'b':'bacon'},
    "hashtags":[
      {"indices":[32,36],"text":"lol"}
    ]
  }
]

tweets = []
for item in data:
  tweet = {}
  all_tags = []
  hashtags = item['hashtags'] #each hashtags is a list
  for tag in hashtags: #{"indices":[32,36],"text":"lol"}
    the_tag = tag['text'] #lol
    all_tags.append(the_tag)
  tweet['hashtags'] = all_tags
  tweets.append(tweet)

print(tweets)




#print(data)

# goal: list of b-words
bwords = []
all_numbers = []

for item in data: #item lookslike {...}
  #inside the loop
  word_dict = item['dict'] # looks like {'a':'aardvark', 'b':'banana'}
  word = item['dict']['b'] #example: 'banana'
  bwords.append(word)

  numbers = item['list'] #list: [1,2,3]
  for num in numbers: #num looks like 1 or 2 or 3
    all_numbers.append(num)



print(bwords)
print(all_numbers)


