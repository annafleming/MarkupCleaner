# MarkupCleaner

Python class for transforming messy markup into digestible HTML blocks (specifically for parsing Indeed.com job descriptions)

## Example

### Input
```
  <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
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
```

### Output

```
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
  <p>Nunc mollis, diam nec eleifend euismod, nunc mi molestie turpis, at elementum sapien turpis nec ante.</p>
  <p>Quisque sit amet volutpat sem, ac pellentesque mauris. Suspendisse potenti.</p>
  <p>Fusce ornare velit eu arcu venenatis, ut tincidunt enim pulvinar.</p>
  <p>Pellentesque non turpis ac purus interdum feugiat.</p>

```


## How to use it?

```
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
    markup_cleaner.reformat(test_text)
```

### Required parameters:
    * tags to replace
    * replacement tag
    * tags to keep unchanged


## Technical requirements

* Python 3.6.3

## License

This project is licensed under the MIT License.
