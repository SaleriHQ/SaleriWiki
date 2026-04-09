# CIS 194: Homework 2 — Algebraic Data Types

> **Due:** Monday, January 28
> **Files to submit:** `LogAnalysis.hs`

---

## Log File Parsing

The log file `error.log` consists of a different log message on each line. Each line begins with a character indicating the type of log message it represents:

- `'I'` for informational messages
- `'W'` for warnings
- `'E'` for errors

Error message lines have an integer indicating the severity of the error (1–100), followed by an integer timestamp and textual content that runs to the end of the line.

### Data Types

```haskell
data MessageType
    = Info
    | Warning
    | Error Int
    deriving (Show, Eq)

type TimeStamp = Int

data LogMessage
    = LogMessage MessageType TimeStamp String
    | Unknown String
    deriving (Show, Eq)
```

Note that `LogMessage` has two constructors: one to represent normally-formatted log messages, and one (`Unknown`) to represent anything else that does not fit the proper format.

### Exercise 1 — `parseMessage`

Define a function that parses an individual line from the log file:

```haskell
parseMessage :: String -> LogMessage
```

**Examples:**

```haskell
parseMessage "E 2 562 help help"
    == LogMessage (Error 2) 562 "help help"

parseMessage "I 29 la la la"
    == LogMessage Info 29 "la la la"

parseMessage "This is not in the right format"
    == Unknown "This is not in the right format"
```

Then define a function to parse an entire log file:

```haskell
parse :: String -> [LogMessage]
```

Use `read`, `lines`, `words`, `unwords`, `take`, `drop`, and function composition (`.`) — don't reinvent the wheel!

---

## Putting the Logs in Order

Log messages are horribly out of order. We use a binary search tree to organize them:

```haskell
data MessageTree = Leaf
    | Node MessageTree LogMessage MessageTree
```

A `MessageTree` is sorted by timestamp: timestamps in any `Node` should be greater than all timestamps in the left subtree, and less than all timestamps in the right child. `Unknown` messages should **not** be stored in a `MessageTree` since they lack a timestamp.

### Exercise 2 — `insert`

```haskell
insert :: LogMessage -> MessageTree -> MessageTree
```

Insert a new `LogMessage` into an existing sorted `MessageTree`, producing a new sorted `MessageTree`. If the message is `Unknown`, return the tree unchanged.

### Exercise 3 — `build`

```haskell
build :: [LogMessage] -> MessageTree
```

Build a complete `MessageTree` from a list of messages by successively inserting them (starting with `Leaf`).

### Exercise 4 — `inOrder`

```haskell
inOrder :: MessageTree -> [LogMessage]
```

Take a sorted `MessageTree` and produce a list of all `LogMessage`s it contains, sorted by timestamp from smallest to biggest. (This is an in-order traversal of the tree.)

Sort and remove unknown messages with:

```haskell
inOrder (build tree)
```

> Note: There are much better ways to sort a list; this is just an exercise to get you working with recursive data structures!

---

## Log File Postmortem

### Exercise 5 — `whatWentWrong`

"Relevant" means "errors with a severity of at least 50."

```haskell
whatWentWrong :: [LogMessage] -> [String]
```

Takes an **unsorted** list of `LogMessage`s and returns a list of messages corresponding to any errors with severity ≥ 50, sorted by timestamp.

**Example:**

Given this log file:

```
I 6 Completed armadillo processing
I 1 Nothing to report
E 99 10 Flange failed!
I 4 Everything normal
I 11 Initiating self-destruct sequence
E 70 3 Way too many pickles
E 65 8 Bad pickle-flange interaction detected
W 5 Flange is due for a check-up
I 7 Out for lunch, back in two time steps
E 20 2 Too many pickles
I 9 Back from lunch
```

The output of `whatWentWrong` should be:

```haskell
[ "Way too many pickles"
, "Bad pickle-flange interaction detected"
, "Flange failed!"
]
```

---

## Miscellaneous

- We will test your solution on log files other than the ones we have given you, so **no hardcoding!**
- You are free (in fact, encouraged) to discuss the assignment with any of your classmates as long as you type up your own solution.

---

## Epilogue

### Exercise 6 (Optional)

For various reasons we are beginning to suspect that the recent mess was caused by a single, egotistical hacker. Can you figure out who did it?
