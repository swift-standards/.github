# Swift Standards

Swift implementations of international standards and protocols — Layer 2 of the [Swift Institute](https://github.com/swift-institute) ecosystem.

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
| [swift-ieee](https://github.com/swift-ieee) · [swift-iec](https://github.com/swift-iec) · [swift-ecma](https://github.com/swift-ecma) · [swift-incits](https://github.com/swift-incits) · [swift-arm-ltd](https://github.com/swift-arm-ltd) · [swift-intel](https://github.com/swift-intel) · [swift-microsoft](https://github.com/swift-microsoft) · swift-riscv (pending) | Single-package organizations |

## Unified packages in this organization

Where several specifications govern the same subject, a `swift-*-standard` package here composes them into one canonical Swift representation. [swift-standards](https://github.com/swift-standards/swift-standards) itself extends the Swift standard library with the functionality every specification package builds on.

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

Each package is a separate Swift Package Manager package with its own repository — there is no umbrella install:

```swift
dependencies: [
    .package(url: "https://github.com/swift-standards/swift-uri-standard.git", from: "0.1.0")
]
```

The per-authority organizations follow the same one-repo-per-package convention. See each package's README for current version and Swift requirements.

## Status

Public alpha. Composition packages are under active development; per-authority organizations are live and filling out.

Maintained by [Coen ten Thije Boonkkamp](https://github.com/coenttb) — contributions welcome via pull request.

## License

All packages use the Apache License 2.0.
