# How to Write Formally Verifiable Specifications in Python 

**Summary:** We can write specifications that are formally verifiable without needing to move away from Python and the benefits that come with it. In this session, we will explore how this can be done. 

**Facilitator:** Roberto Saltini

**Note Taker:** TBD

**Pre-Reads:** 
- [Draft 3SF Specification Documentation](https://github.com/saltiniroberto/ssf/tree/separate_bft/high_level/README.md)
- [ethresear.ch post on 3SF](https://ethresear.ch/t/3-slot-finality-ssf-is-not-about-single-slot/20927)

**[Draft Slides](https://docs.google.com/presentation/d/1xtKPqN9KnMnIZfbl-7A7C7L9-ynJKVlpmmtD4UfMVtQ)**

## Agenda 

- Presentation
    - Pitfalls in the way the current specification are written and how to avoid it
    - Walk through a practical example: [the draft 3SF specification](https://github.com/saltiniroberto/ssf/tree/separate_bft/high_level/README.md)
- Open Discussion 
    - Is the resulting spec readable enough?
    - How can we improve readability without sacrificing formal verifiability
    - Alternative approaches



## Notes & Action Items 

# Problem: Mutable objects

Due to [aliasing](https://en.wikipedia.org/wiki/Aliasing_(computing)), writing to a reference may implicitly modify values obtained via other references. In the F/V context, it invalidates what we know about affected memory locations. Tracking aliasing and re-establishing properties can significantly complicate reasoning.

## Solution

Use immutable objects (non-destructive updates). Can be facilitated by [pyrsistent](https://github.com/tobgu/pyrsistent/) library.

Concerns:
- non-destructive updates are less readable, especially in case of nested updates ([example](https://github.com/saltiniroberto/ssf/blob/ad3ba2c21bc1cd554a870a6e0e4d87040558e129/high_level/protocols/rlmd/3sf_high_level.py#L187))
- MyPy typechecking fails for `PRecord` objects (can be fixed with a custom [MyPy plugin](https://github.com/saltiniroberto/ssf/blob/ad3ba2c21bc1cd554a870a6e0e4d87040558e129/my_plugin.py))

## More involved solution

Allow mutatable objects, but only when it's "safe" (e.g. allow only exclusive mutable references, similar to Rust's [Mutable references](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#mutable-references)).

And then mechanically transform destructive updates to non-destructive ones (see [“Mutable Forest” Memory Model for blockchain specs](https://ethresear.ch/t/mutable-forest-memory-model-for-blockchain-specs/10882) for more details).

E.g. 
```
node_state.buffer_blocks[block_hash(block)] = block
```
becomes
```
node_state = node_state.set(
        buffer_blocks=pmap_set(
            node_state.buffer_blocks,
            block_hash(block),
            block)
    )
```
assuming that the `node_state` is an exclusive reference.

Concerns:
- non-trivial to implement
- semantics might be "surprising" to Python users

---

# Problem: Python semantics is quite complex and not formally defined

## Solution

Use a very limited subset of Python
- `if`
- `for`
- function calls (not method calls)
- `lambda`s

Comments from @ericsson49:
- Python closures are [late binding](https://docs.python-guide.org/writing/gotchas/#late-binding-closures), which can be a problem when translating lambdas (and inner functions) to F/V languages. One solution is to allow access to immutable outer variables only
- method calls can be allowed too, e.g. when it doesn't involve virtual method dispatch
    - `pset_add(some_set, some_value)` can be replaced with `some_set.add(some_value)`
- `while` loops should be okay too. In practice, recursion is already present in the 3SF specs, so why exclusing `while` loops?
- [walrus operator](https://peps.python.org/pep-0572/) (`a := expr`) is a big problem for transpilation, though it's not used in specs currently
- an additional suggestion for lambdas is to use them only, when they are immediately inlineable (e.g. `map`, `filter`, `sorted`, `max/min` and similar)
- list/set comprehnsions should be okay too (can desugar them to `map/filter`, albeit it can affect semantics in edge cases (e.g. when using walrus operator))

---

# Problem: Significant parts of the specs are in natural language

## Solution (for "honest validator" part)

Specify the “honest validator” behaviour in code.

A comment from @ericsson49:
> in general, specs may have non-deterministic aspects. But it conflicts with executability of specs (which is a highly desireable property). This might be a reason for specifying parts of specs in prose.
>
> That suggests a new challenge: how to specify non-determinism in python, but keep specs "executable" (e.g. for test generation).

## LLMs and CNLs

Were discussing [Large Language Models](https://en.wikipedia.org/wiki/Large_language_model) and [Controlled Natural Language](https://en.wikipedia.org/wiki/Controlled_natural_language) as potential ways to mitigate the problem.

E.g. use LLM to translate prose to a formal language (can be challenging). Or re-write prose using a formally defined controlled language (challenging too).

Some links:
[SAD](http://nevidal.org/sad.en.html) and [ForTheL](http://nevidal.org/download/forthel.pdf)
[Naproche](https://naproche.github.io/)

---

# Problem: Mixing concerns for external behaviour with concerns for efficiency

## Solution

2 specs at 2 different level of abstractions: high level vs lower-level specs

A comment from @ericsson49
> The high level spec doesn't have to be deterministic, which allows to express more spec parts formally (opposed to natural language), e.g. network layer related specs. A non-deterministic spec can still be used to check traces (and perhaps even to sample test vectors).




