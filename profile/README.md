# Swift Standards

Swift implementations of international standards and protocols — Layer 3 of the [Swift Institute](https://github.com/swift-institute) ecosystem.

## What this is

Authoritative specifications — RFCs, ISO standards, W3C and WHATWG specs — modeled directly in Swift's type system, so parsing, validation, and formatting are enforced by the compiler rather than checked at runtime. Each specification lives in its own package, defines its own namespace (`RFC_5322`, `ISO_32000`), and follows its source document as literally as possible.

## The authorities

Each standards authority has its own GitHub organization hosting the specifications it governs:

| Organization | Covers |
|---|---|
| [swift-ietf](https://github.com/swift-ietf) | IETF RFCs — URI, IP, email, sockets, UUID |
| [swift-iso](https://github.com/swift-iso) | ISO — PDF, EPUB, date and time, locale |
| [swift-w3c](https://github.com/swift-w3c) | W3C — CSS, SVG |
| [swift-whatwg](https://github.com/swift-whatwg) | WHATWG — HTML, the URL Living Standard |
| [swift-ieee](https://github.com/swift-ieee) · [swift-iec](https://github.com/swift-iec) · [swift-ecma](https://github.com/swift-ecma) · [swift-incits](https://github.com/swift-incits) · [swift-arm-ltd](https://github.com/swift-arm-ltd) · [swift-intel](https://github.com/swift-intel) · [swift-microsoft](https://github.com/swift-microsoft) · [swift-riscv](https://github.com/swift-riscv) · [swift-bipm](https://github.com/swift-bipm) | Single-package organizations |
| [swift-linux-foundation](https://github.com/swift-linux-foundation) | Linux Foundation — Linux standard, Model Context Protocol |

## Browse the packages

Where several specifications govern the same subject, a `swift-*-standard` package here
composes them into one canonical, policy-free Swift representation. It absorbs revisions of
the underlying specifications, so code that depends on it does not have to change.

Use GitHub's native [repository view](https://github.com/orgs/swift-standards/repositories) to
browse the current package set and each repository's description, or start with the native
[repositories matching `swift-`](https://github.com/orgs/swift-standards/repositories?q=swift-&type=all)
and [repositories matching `standard`](https://github.com/orgs/swift-standards/repositories?q=standard&type=all)
filters. The view can be narrowed further with GitHub's repository search. The
per-authority organizations above remain the source for specification-specific packages.

## How to use a package

Each package is a separate Swift Package Manager package with its own repository — there is no umbrella install:

```swift
dependencies: [
    .package(url: "https://github.com/swift-standards/swift-uri-standard.git", branch: "main")
]
```

The per-authority organizations follow the same one-repo-per-package convention. See each package's README for current version and Swift requirements.

Maintained by [Coen ten Thije Boonkkamp](https://github.com/coenttb) — contributions welcome via pull request.

## License

All packages use the Apache License 2.0.
