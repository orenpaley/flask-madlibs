"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

    def getWords(self):
      return self.prompts

    def getTemplate(self):
        return self.template
      


"""Madlibs Stories."""

STORIES = []

STORIES.append(Story(
    ["adjective", "plural_noun", "verb", "place"],
    """My {adjective} {plural_noun} like to {verb} when they go to {place}."""))

STORIES.append(Story(
    ["setting", "big_noun", "fun_verb", "cool_adjective", "plural_noun"],
    """Once upon a time in a long-ago {setting}, there lived a
       large {cool_adjective} {big_noun}. It loved to {fun_verb} {plural_noun}."""))

STORIES.append(Story(
    ["place", "plural_noun", "verb", "plural_noun2", "adjective"],
    """In {place}, {plural_noun} are known to {verb} around {plural_noun2} 
    when they feel {adjective}."""))

STORIES.append(Story(
    ["name", "gerund", "plural_noun", "verb"],
    """When {name} goes {gerund}, they tend to forget about the {plural_noun} that 
    {verb} nearby."""))


