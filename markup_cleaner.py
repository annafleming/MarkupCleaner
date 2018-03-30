import re

class MarkupCleaner:

    def __init__(self, remove_tags, rewrite_with_tag, keep_tags):
        self._remove_tags = remove_tags
        self._rewrite_with_tag = rewrite_with_tag
        self._keep_tags = keep_tags

    def reformat(self, text):
        text_without_line_breaks = self._remove_line_breaks(text)
        text_with_replaced_tags = self._replace_tags(text_without_line_breaks)
        text_with_separated_remaining_tags = self._separate_remaining_tags(text_with_replaced_tags)
        text_with_removed_duplicate_linebreaks = self._remove_duplicates('<br/>', text_with_separated_remaining_tags)
        return self._wrap_in_tag(text_with_removed_duplicate_linebreaks)

    def _remove_line_breaks(self, text):
        return text.replace('\n','').replace('\r','')

    def _replace_tags(self, text):
        regex = re.compile('</?(' + '|'.join(self._remove_tags)+')>')
        return re.sub(regex,'<br/>', text)

    def _separate_remaining_tags(self, text):
        result = text
        for tag_name in self._keep_tags:
            tag, closing_tag = self._create_tags(tag_name, True)
            result = result.replace(tag,'<br/>' + tag).replace(closing_tag, closing_tag + '<br/>')
        return result

    def _create_tags(self, tag_name, closing = False):
        tag = '<' + tag_name + '>'
        if closing:
            return (tag, '</' + tag[1:])
        else:
            return tag

    def _remove_duplicates(self, tag, text):
        regex = re.compile('(' + tag + ')+')
        return re.sub(regex, tag, text)

    def _wrap_in_tag(self, text):
        text_paragraphs = text.strip('<br/>').split('<br/>')
        tag, closing_tag = self._create_tags(self._rewrite_with_tag, True)
        pattern = re.compile('<(' + '|'.join(self._keep_tags)+')')
        new_blocks = list(map(lambda x: tag + x + closing_tag if not re.match(pattern, x) else x, text_paragraphs))
        return ''.join(new_blocks)
