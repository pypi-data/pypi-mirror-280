from nltk.tokenize import word_tokenize
from nltk.parse.corenlp import CoreNLPParser
import re

class PassivePhraseExtractor:
    def __init__(self, parser_url='http://localhost:9000'):
        self.pos_parser = CoreNLPParser(url=parser_url, tagtype='pos')
        self.modal_verbs = ['can', 'could', 'shall', 'should', 'may', 'might']
    
    def extract_passive_phrases_from_dict(self, passive_sentences):
        extracted_verbs = {}
        for tense, clauses in passive_sentences.items():
            tense_verbs = []
            for clause in clauses:
                full_phrase = self._get_verbs(clause)
                if 'Future' in tense:
                    full_phrase = self._add_will_to_future(full_phrase.split())
                if full_phrase:
                    tense_verbs.append(full_phrase)
            if tense_verbs:
                extracted_verbs[tense] = tense_verbs
        return extracted_verbs
    
    def _get_verbs(self, clause):
        words = word_tokenize(clause)
        pos_tags = self.pos_parser.tag(words)
        aux_verbs = []
        main_verbs = []
        negation = False
        aux_indices = []

        for i, (word, tag) in enumerate(pos_tags):
            if word.lower() in ["not", "n't"]:
                negation = True
            elif word.lower() in self.modal_verbs or word.lower() in ['is', 'are', 'am', 'was', 'were', 'be', 'been', 'being', 'has', 'have', "'ve", 'had', 'will', "'ll", 'could', 'can', 'shall', 'should', 'will', 'would']:
                aux_verbs.append(word)
                aux_indices.append(i)
            elif tag == 'VBN':
                main_verbs.append(word)

        if negation:
            # Use regex to insert 'not' after the first auxiliary verb
            if aux_verbs:
                pattern = re.compile(r'(' + '|'.join(re.escape(aux) for aux in aux_verbs) + r')')
                clause = pattern.sub(r'\1 not', clause, count=1)
                aux_verbs.insert(1, 'not')

        try:
            if aux_indices:
                start = aux_indices[0]
                end = len(words)
                for main_verb in main_verbs:
                    if main_verb in words[aux_indices[0]:]:
                        end = words.index(main_verb) + 1
                        break
                full_phrase = ' '.join(words[start:end])
            else:
                full_phrase = ' '.join(aux_verbs + main_verbs)
        except ValueError as e:
            print(f"Error processing clause '{clause}': {e}")
            full_phrase = ' '.join(aux_verbs + main_verbs)

        return full_phrase
    
    def _add_will_to_future(self, aux_verbs):
        if 'will' not in aux_verbs:
            aux_verbs.insert(0, 'will')
        return ' '.join(aux_verbs)