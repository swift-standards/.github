# Swift Standards

Swift implementations of international standards and protocols — modular packages that model authoritative specifications directly in Swift's type system, with parsing, validation, and formatting enforced by the compiler rather than at runtime.

## Part of Swift Institute

swift-standards is the Layer 2 organization within the [Swift Institute](https://github.com/swift-institute) ecosystem — specification implementations that depend on swift-primitives (Layer 1) and feed into swift-foundations (Layer 3). It is an organization of organizations: this org hosts unified, final-type composition packages drawing from per-authority sub-orgs (swift-ietf for RFCs, swift-iso for ISO specs, swift-w3c, swift-whatwg, plus single-package organizations for IEEE, IEC, ECMA, INCITS, ARM, Intel, RISC-V, Microsoft). See the [ecosystem overview](https://github.com/swift-institute) and [layered architecture](https://swift-institute.org) for context.

## Technical Approach

Newer standards may depend on older ones. Each standards package depends solely on the swift-standards package. This core package extends Swift’s standard library with foundational functionality common to many specifications.

Every standard defines its own namespace (e.g. RFC_5322) and nests all of its types within that namespace. Standards may extend Swift’s standard library types where appropriate. Cross-type transformations occur only through init extensions or static funcs; methods are reserved for mutation, returning Self, or limited conveniences.

Each standards package implements its authoritative source document as literally as possible. Parsing, validation, and formatting are performed through Swift’s type system, ensuring that invalid structures are rejected at compile time rather than runtime. Packages consider performance, such as by using `[UInt8]` instead of `String` where appropriate.

Where multiple specifications govern the same subject matter, a dedicated swift-*-standard package brings them together. This package depends on all relevant standards and exposes a unified, final type to be used as the canonical representation.

## Companion organizations

Each spec authority has its own GitHub organization hosting the per-spec packages it governs. swift-standards depends on these directly and composes them into the unified packages listed below.

| Organization | Role |
|---|---|
| [swift-ietf](https://github.com/swift-ietf) | IETF RFCs (URI, IP, email, sockets, etc.) |
| [swift-iso](https://github.com/swift-iso) | ISO specifications (PDF, EPUB, date/time, locale) |
| [swift-w3c](https://github.com/swift-w3c) | W3C specifications (CSS, SVG) |
| [swift-whatwg](https://github.com/swift-whatwg) | WHATWG specifications (HTML, URL Living Standard) |
| [swift-ieee](https://github.com/swift-ieee), [swift-iec](https://github.com/swift-iec), [swift-ecma](https://github.com/swift-ecma), [swift-incits](https://github.com/swift-incits), [swift-arm-ltd](https://github.com/swift-arm-ltd), [swift-intel](https://github.com/swift-intel), [swift-riscv](https://github.com/swift-riscv), [swift-microsoft](https://github.com/swift-microsoft) | Single-package per-authority organizations |

Some links may currently 404 — the per-authority organizations are being released over the coming weeks alongside this umbrella.

## Packages in this organization

This organization hosts the unified, final-type composition packages listed below. Each draws from one or more per-authority specifications and exposes a single canonical Swift representation.

| Package | Role |
|---|---|
| [swift-color-standard](https://github.com/swift-standards/swift-color-standard) | Unified color representation across CSS / display profiles |
| [swift-css-standard](https://github.com/swift-standards/swift-css-standard) | CSS specification — selectors, properties, values |
| [swift-darwin-standard](https://github.com/swift-standards/swift-darwin-standard) | Darwin platform specification surface |
| [swift-domain-standard](https://github.com/swift-standards/swift-domain-standard) | Domain name representation (per RFC 1035 et seq.) |
| [swift-email-standard](https://github.com/swift-standards/swift-email-standard) | Email message format |
| [swift-emailaddress-standard](https://github.com/swift-standards/swift-emailaddress-standard) | Email address (RFC 5322) |
| [swift-epub-standard](https://github.com/swift-standards/swift-epub-standard) | EPUB publication format |
| [swift-html-standard](https://github.com/swift-standards/swift-html-standard) | HTML — unified across W3C historical and WHATWG living standard |
| [swift-ipv4-standard](https://github.com/swift-standards/swift-ipv4-standard) | IPv4 address |
| [swift-ipv6-standard](https://github.com/swift-standards/swift-ipv6-standard) | IPv6 address |
| [swift-json-feed-standard](https://github.com/swift-standards/swift-json-feed-standard) | JSON Feed specification |
| [swift-locale-standard](https://github.com/swift-standards/swift-locale-standard) | Locale identifier (BCP 47, ISO 639/3166) |
| [swift-pdf-standard](https://github.com/swift-standards/swift-pdf-standard) | PDF specification (ISO 32000) |
| [swift-postgresql-standard](https://github.com/swift-standards/swift-postgresql-standard) | PostgreSQL wire/SQL specification |
| [swift-rss-standard](https://github.com/swift-standards/swift-rss-standard) | RSS specification |
| [swift-sockets-standard](https://github.com/swift-standards/swift-sockets-standard) | Sockets specification |
| [swift-svg-standard](https://github.com/swift-standards/swift-svg-standard) | SVG specification |
| [swift-time-standard](https://github.com/swift-standards/swift-time-standard) | Time representation (ISO 8601 et seq.) |
| [swift-uri-standard](https://github.com/swift-standards/swift-uri-standard) | URI Generic Syntax (RFC 3986) |

## How to use a package

Each package in this organization is a separate Swift Package Manager package with its own GitHub repo — there is no umbrella swift-standards package. To depend on a package, use its individual repository URL:

```swift
dependencies: [
    .package(url: "https://github.com/swift-standards/swift-uri-standard.git", from: "0.1.0")
]
```

See each package's README for current version, target configuration, and Swift version requirements. The per-authority sub-orgs (swift-ietf, swift-iso, etc.) follow the same one-repo-per-package convention.

## Status

Initial public alpha. Composition packages are at status `active--development`. Per-authority sub-orgs are being released over the coming weeks; some links above may currently 404 until those orgs publish their first packages.

Maintained by [Coen ten Thije Boonkkamp](https://github.com/coenttb) — contributions welcome via pull request to individual package repositories.

## License

All packages use the Apache License 2.0.
