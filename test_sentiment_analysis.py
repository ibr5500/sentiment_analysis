import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalysis(unittest.TestCase):
  def test_sentiment_analyzer_1(self):

    # Test case for positive sentiment
    result_1 = sentiment_analyzer('I love working with Python')
    self.assertEqual(result_1['label'], 'SENT_POSITIVE')
    
    # Test case for negative sentiment
    result_2 = sentiment_analyzer('I hate working with Python')
    self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
    
    # Test case for neutral sentiment
    result_3 = sentiment_analyzer('I am neutral on Python')
    self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()