############################################################################################################################################################
# Supervised Learning

# Spam Classifier (Naive Bayes Classifier)

# Training the model
# 1. Calculate for each word in each email the number of times the word appears in ham or spam email. Cspam(T) & Cham(T)
# 2. Cspam(T) : How many spam messages contain the word T
# 3. Cham(T) : Hom many ham messages contain  the word T
# 4. Find Spamminess of each word S[T] = Cspam(T) / (Cspam(T) + Cham(T))

# Running the model
# 1. Look up spamminess of each word
# 2. Find total spamminess of the message S[M]
# 3. Find total hamminess of the message H[M] = (1-S[M])
# 4. If S[M] > H[M] then "SPAM" else "HAM

############################################################################################################################################################


