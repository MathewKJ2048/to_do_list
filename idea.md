
## Scope:

- do one thing and do it well, no link to time
- cross scripting can be done as needed

## Architecture:

- each entity is a task
- each task can have subtasks
- thus a tree-like stucture is best
- each leaf is an atomic task, either complete or not

## Features:

- some form of history for completed tasks
- operations: insert task, delete task, nothing else

## Design decisions:

- terminal-based, no use of mouse
- can use ncurses for clean UI, 
- called by a simple command `todo`
- ctrl-X or ctrl-C for exit
- two modes - add and mark
- when marking, delete does the marking
- when adding, typing does the thing as normal, then ctrl-S adds it
- each add event and delete event is added into a log file
- tasks are ordered, so implemented via lists

## navigating tree structure:

- left for parent, right for child
- up and down to move along list
- two pointers - root and selector
- ctrl+ will go one root in
- ctrl- will go one out

## Creation:

- Shift + right makes new child at top of list
- Shift plus up makes sibling above
- Shift plus down makes sibling below
