import argparse


def write_story(prompt):
    return f"""
Creative Story
==============

Prompt: {prompt}

On an ordinary day, something unexpected happened.

The main character had never imagined that a simple moment could
turn into such an interesting adventure. Curious and determined,
they decided to follow the mystery instead of turning back.

What happened next became a story that would never be forgotten.
"""


def write_poem(prompt):
    return f"""
Creative Poem
=============

Prompt: {prompt}

A quiet moment begins,
A thought becomes a dream,
The world changes slowly,
Nothing is quite as it seems.

Inspired by: {prompt}
"""


def write_scene(prompt):
    return f"""
Creative Scene
==============

Prompt: {prompt}

[The scene begins.]

CHARACTER 1:
I didn't expect to find this here.

CHARACTER 2:
Neither did I. But now that we're here,
we need to find out what it means.

[They look at the mysterious discovery.]

CHARACTER 1:
Then let's begin.

[Scene ends.]
"""


def main():
    parser = argparse.ArgumentParser(
        description="Creative Writer CLI"
    )

    parser.add_argument(
        "--type",
        choices=["story", "poem", "scene"],
        required=True,
        help="Type of creative writing"
    )

    parser.add_argument(
        "--prompt",
        required=True,
        help="Topic or idea for the writing"
    )

    args = parser.parse_args()

    if args.type == "story":
        result = write_story(args.prompt)
    elif args.type == "poem":
        result = write_poem(args.prompt)
    else:
        result = write_scene(args.prompt)

    print(result)


if __name__ == "__main__":
    main()
