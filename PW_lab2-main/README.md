# Lab 2 - Self-made browser

## Story

Imagine, you're a developer at TwoLines GmbH, a startup from Zurich, Switzerland. The idea of the startup is pretty simple - you develop best-in-class browser experience, with privacy and security in mind. One day, you receive a message from the CTO, Mike.

```
Hey there!

Tomorrow we'll have a presentation for a really biiiig inv  estor.
They say they don't need PPTs.
They want at least some proof-of-concept for secure browsers for their toasters.
Can you share with me the executable we used last time for demo?

Cheers,
Mike
```

Yeah, the catch is, browser exeprience for toasters.
Nonetheless, you can't remember where you've saved the executable, so you start writing it from scratch.

## Task

1. You have to write a command line program, using [go2web](go2web) as a starting point;
2. The program should implement the following CLI:
  ```
  go2web -u <URL>         # make an HTTP request to URL and print the response
  go2web -s <search-term> # search the term using your favorite search engine and print top 10 results
  go2web -h               # show help
  ```
3. The responses from requets should be human-readable (e.g. no HTML tags in the output)
3. Add another option to the program, to impress that biiiig investor.

## Special conditions

You can use any programming language, but not the built-in/third-party libraries for making HTTP requests. You can't build a GUI application.

## Grading

Points:

- executable with basic 1 command & help - `5` points
- executable with 2 commands & help - `7` points
- executable with 1 additional option - `+1` point

You can get `+1` extra point if HTML response is beautifully formatted.
You can get `+2` extra points if results from search engine can be accessed somehow.
You can get `+2` extra points for implementing a cache mechanism.

## Hints

- Before opting for some language X, make sure you have the right tools: CLI parser, HTML parser, TCP sockets;
- For CLI you can use built-in libraries;
- Use third-party libraries for parsing HTML and presenting it;
- While developing, you can launch a local server using `python3 -m http.server`, to test & debug the app.
