def remove(article_text):
    noise_words = [
        "KAMI",
        "PAY ATTENTION:", "PAY ATTENTION",
        ": Follow us on", "Instagram",
        "- get the most important news directly in your favourite app!",
        "Source: KAMI.com.gh",
        "Like and share our Facebook posts to support the KAMI team! Share your thoughts in the comments. We love reading them!",
        "Like and share our",
        "Facebook posts",
        "to support the KAMI team! Share your thoughts in the comments. We love reading them!",
        "Click", '"See First" under the "Following" tab to see KAMI news on your News Feed',
        'Click "See First" under the "Following" tab to see KAMI news on your News Feed',
        'Click "See first" under the "Following" tab to see KAMI news on your Newsfeed',
        'Click "See First" under the "Following" tab to see KAMI news on your News Feed!',
        'Click "See First" under the "Following" tab to see',
        "Tingnan ang mga balitang para sa'yo ➡️ hanapin ang \"Recommended for you\" block at mag-enjoy!",
        "Update KAMI App now: the old version will be disabled on June, 15!"
    ]

    return list(filter(lambda x: x.strip() not in noise_words, article_text))