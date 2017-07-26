from textrazor import TextRazor
from pprint import pprint as pp

API_KEY = "8ca44890eb757ac572861b40845e88e5fdb65d2894acc9cac9ac3d20"   

class RelationResult:
    def __init__(self, predicate_positions, predicate_words, property_positions, property_words):
      self.predicate_positions_ = predicate_positions
      self.predicate = predicate_words
      self.property_positions_ = property_positions
      self.property = property_words
      
    def __str__( self):
        return self.predicate+' --> '+self.property
    
    def __repr__(self):
        return self.__str__()
      
def getBinaryRelations(string,extractors=["words", "relations"]):
    client = TextRazor(API_KEY,extractors=extractors)
    response = client.analyze(string)
    result = []
    root = [w.token for w in response.words() if w.parent_position is None]
    for relation in response.properties():
        result.append(RelationResult(relation.predicate_positions,' '.join([w.token for w in relation.predicate_words]),relation.property_positions,' '.join([w.token for w in relation.property_words])))      
    return result, root
        
if __name__ == "__main__":
    pp(getBinaryRelations(string='On which team does Ronaldo plays'))