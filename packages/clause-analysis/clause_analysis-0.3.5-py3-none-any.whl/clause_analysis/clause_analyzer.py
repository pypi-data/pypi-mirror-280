import re
from nltk.tokenize import sent_tokenize
import spacy

class ClauseAnalyzer:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.active_clauses = []
        self.passive_clauses = []
        self.conjunctions_and_connectors = [
            "and", "but", "or", "nor", "for", "so", "yet",
            "after", "although", "as", "because", "before", "even if", "even though", 
            "if", "once", "provided that", "rather than", "since", 
            "so that", "than", "that", "though", "unless", "until", "when", "whenever", 
            "where", "whereas", "wherever", "whether", "while", 'who',
            "accordingly", "anyway", "besides", "certainly", "consequently", "finally", 
            "furthermore", "hence", "however", "indeed", "instead", "likewise", "meanwhile", 
            "moreover", "nevertheless", "next", "nonetheless", "otherwise", "similarly", "still", 
            "then", "therefore", "thus",
            "after", "before", "since", "until", "how", "by", "By", "simply", "to"
        ]
    
    def split_clauses(self, text):
        sentences = sent_tokenize(text)
        result = []
        
        for sentence in sentences:
            doc = self.nlp(sentence)
            clauses = []
            current_clause = []
            verb_count = 0
            
            for token in doc:
                current_clause.append(token.text)
                if token.pos_ == "VERB":
                    verb_count += 1
                
                if token.text in self.conjunctions_and_connectors or verb_count > 1:
                    if verb_count > 1:
                        # Remove the last verb from current clause and start a new clause
                        new_clause = " ".join(current_clause[:current_clause.index(token.text)]).strip()
                        if new_clause and new_clause != '.':
                            clauses.append(new_clause)
                        current_clause = [token.text]  # Keep the conjunction in the next clause
                        verb_count = 1  # Reset verb count for new clause
                    else:
                        clauses.append(" ".join(current_clause).strip())
                        current_clause = [token.text]  # Keep the conjunction in the next clause
                        verb_count = 0 if token.pos_ != "VERB" else 1
            
            if current_clause:
                final_clause = " ".join(current_clause).strip()
                if final_clause != '.':
                    clauses.append(final_clause)
            
            result.extend(clauses)
        
        # ลบประโยคที่เริ่มต้นด้วย "to"
        result = [clause for clause in result if not clause.lower().startswith('to ')]
        return result
    
    def search_tense_aspects(self, clauses):
        for sentence in clauses:
            doc = self.nlp(sentence)
            is_passive = any(token.dep_ == 'auxpass' for token in doc)
            
            if is_passive:
                self.passive_clauses.append(sentence)
            else:
                self.active_clauses.append(sentence)

    def analyze(self, text):
        self.active_clauses = []
        self.passive_clauses = []
        
        clauses = self.split_clauses(text)
        self.search_tense_aspects(clauses)
        
        return self.active_clauses, self.passive_clauses

    def remove_initial_conjunctions(self, clauses):
        pattern = r'^\b(' + '|'.join(map(re.escape, self.conjunctions_and_connectors)) + r')\b\s*'
        cleaned_clauses = [re.sub(pattern, '', clause) for clause in clauses]
        return cleaned_clauses