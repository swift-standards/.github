# Swift Standards

Swift implementations of standards and protocols.

## Overview

Rules sit at the heart of every system we build and rely on. When those rules are clear and consistently expressed, everything built atop them becomes simpler, safer, and more predictable. We believe rules deserve to be written in a form that leaves no ambiguity — where structure, constraints, and intent can be validated rather than interpreted.

Swift’s type system makes that possible. By modeling the logic of standards directly in types, authoritative specifications become precise, executable rules that the compiler can enforce. This removes guesswork, prevents invalid states, and forms a foundation developers can trust.

Swift Standards is built on that idea. It offers a growing collection of modular Swift packages that implement international standards exactly as written, each grounded in a shared core. Together, these packages create a reliable, composable base for software that needs to follow the rules — both today and in the systems yet to come.

## Technical Approach

Newer standards may depend on older ones. Each standards package depends solely on the swift-standards package. This core package extends Swift’s standard library with foundational functionality common to many specifications.

Every standard defines its own namespace (e.g. RFC_5322) and nests all of its types within that namespace. Standards may extend Swift’s standard library types where appropriate. Cross-type transformations occur only through init extensions or static funcs; methods are reserved for mutation, returning Self, or limited conveniences.

Each standards package implements its authoritative source document as literally as possible. Parsing, validation, and formatting are performed through Swift’s type system, ensuring that invalid structures are rejected at compile time rather than runtime. Packages consider performance, such as by using `[UInt8]` instead of `String` where appropriate.

Where multiple specifications govern the same subject matter, a dedicated swift-*-standard package brings them together. This package depends on all relevant standards and exposes a unified, final type to be used as the canonical representation.

## Requirements
	•	Swift 6.2+
	•	macOS 15.0+ / iOS 18.0+ / Linux

## License

All packages use the Apache License 2.0.
