import language_tool_python
import enchant
import re

class SpellCheckerModule:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')
        self.d = enchant.Dict("en_US")  # Dictionary for additional spell checking

    def correct_spell(self, text):
        # Use regex to find words and preserve spaces and punctuation
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
        corrected_words = []
        mistakes = []

        # Maintain the original spacing and punctuation by capturing and handling them separately
        space_and_punctuation_pattern = r'(\s+|[^\w\s]+)'
        parts = re.split(space_and_punctuation_pattern, text)
        new_parts = []

        for part in parts:
            if part and re.fullmatch(r'\w+', part) and not self.d.check(part):
                suggestions = self.d.suggest(part)
                if suggestions:
                    new_parts.append(suggestions[0])
                    mistakes.append((part, suggestions[0]))  # Track original and corrected
                else:
                    new_parts.append(part)
            else:
                new_parts.append(part)

        intermediate_text = ''.join(new_parts)

        # Now use LanguageTool to check the text with corrected spelling
        matches = self.tool.check(intermediate_text)
        final_text = language_tool_python.utils.correct(intermediate_text, matches)

        # Analyze changes made by LanguageTool
        for match in matches:
            original_text_segment = intermediate_text[match.offset:match.offset + match.errorLength]
            corrected_segment = match.replacements[0] if match.replacements else original_text_segment
            if original_text_segment != corrected_segment:
                mistakes.append((original_text_segment, corrected_segment))

        return final_text, mistakes

    def correct_text_from_file(self, text):
        # This function uses the same logic as correct_spell but is specifically named to indicate usage for file inputs
        return self.correct_spell(text)

    def correct_grammar(self, text):
        matches = self.tool.check(text)
        found_mistakes = [text[match.offset:match.offset + match.errorLength] for match in matches]
        corrected_text = language_tool_python.utils.correct(text, matches)
        return corrected_text, found_mistakes if found_mistakes else "No grammar mistakes found."