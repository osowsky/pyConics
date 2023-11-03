# Changelog

<!--next-version-placeholder-->

## v1.0.1 (02/11/2023)

- The dot() function in utils.py had a bug that was fixed.
- The images in README.md had unresolved links. This bug
was fixed.

## v1.0.0 (23/10/2023)

- pyConics classes have been renamed by adding a prefix C in
front of every class name, i.e., Point class has become CPoint
and Line class has become CLine.
- CFigure and CAxes classes have been created. Thus, they can
be used to plot CPoint, CLine and in the future CConic.
- A bug was fixed in utils.dot() method.
- function.py has been renamed to utils.py.
- requirement: python version was downgraded to 2.10.
- requirement: numpy version was downgraded to 1.25.

## v0.2.6 (20/10/2023)

- A dependency conflict has been resolved.

## v0.2.5 (20/10/2023)

- A bug has been fixed in README.md.

## v0.2.0 (20/10/2023)

- First release of `pyConics`!

## v0.1.1-beta (16/10/2023)

- Fix circular import exceptions in .py files, by using
TYPE_CHECKING constant from typing module.

## v0.1.0-beta (14/10/2023)

- New methods have been added in Point and Line classes.
Point class: are_coincident() method.
Line class: are_coincident() and are_concurrent() methods.

## v0.0.1-beta (13/10/2023)

- First pre-release of `pyConics`!
