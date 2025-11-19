# Swift Standards

Type-safe implementations of internet standards (RFCs) as Swift packages.

## Overview

Swift Standards provides Swift implementations of standards and protocols. Each package implements a specific standard with Swift's type system, enabling compile-time validation instead of runtime string parsing.

## Technical Approach

Chronologically newer standards may depend on older standards. Each standard package depends solely on the `swift-standards` package. `swift-standards` extends the Swift standard library types with functionality that is foundational to standards.

Standards declare a namespace (e.g. RFC_5322), and must nest all their types under that namespace. Standards may extend Swift standard library types where appropriate. Type transformations must occur solely via extension `init`s, or via `static func`s. Methods are for mutation, returning Self, or - in limited cases - conveniences.

All standards packages must implement the specification as literally written in the authoritative document for that standard. 

All implementations use Swift's type system for validation, parsing, and formatting. Invalid data structures should be rejected at compile time rather than runtime.

Where multiple standards are authoritative with respect to the same subject matter, we introduce a swift-*-standard package, which depends on all standards relevant to the subject matter, and which provides a final type to be used as a standard.

## Requirements

- Swift 6.2+
- macOS 15.0+ / iOS 18.0+ / Linux

## License

All packages use Apache License 2.0.
