from markup_cleaner import MarkupCleaner


test_text = """<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
<br/>
<br/>
Nunc mollis, diam nec eleifend euismod, nunc mi molestie turpis, at elementum sapien turpis nec ante.
</div>
<br/>
<br/>
Quisque sit amet volutpat sem, ac pellentesque mauris. Suspendisse potenti.
<p>
Fusce ornare velit eu arcu venenatis, ut tincidunt enim pulvinar.
<br/>
<br/>
Pellentesque non turpis ac purus interdum feugiat.
</p>
"""


markup_cleaner = MarkupCleaner(['div', 'p', 'h1', 'h2', 'h3', 'h4', 'h5'], 'p', ['ul'])
print(markup_cleaner.reformat(test_text))
