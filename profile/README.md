# Swift Web Standards

**Building Swift's Web Foundation**

The web runs on standards—RFCs that define how URLs work, how email is formatted, how HTTP requests are structured. But for Swift developers, these standards have been locked behind string parsing and runtime validation. Until now.

Swift Web Standards implements internet protocols as type-safe Swift packages. Not approximations. Not wrappers. Full RFC compliance with compile-time guarantees.

## Why This Exists

Every web framework reinvents the same wheels. URL parsing. Email validation. Form data handling. HTTP header parsing. Each implementation slightly different, each validated at runtime, each catching errors when it's too late.

The problem isn't that these solutions work poorly. The problem is they work at runtime, when the cost of failure is highest. They validate when they should prevent. They parse when they should compose.

Swift's type system can do better. The language that brought us type-safe UI construction, type-safe database queries, and type-safe concurrency can bring the same guarantees to internet standards.

## What We're Building

We implement RFCs as pure Swift types. Each standard becomes a package with compile-time guarantees:

**URI Standards** - Parse, manipulate, and generate URIs with full RFC 3986, 3987, and 6570 compliance. URI templates become type-safe with variable expansion validated at compile time.

**Email Standards** - Email addresses validated across multiple RFCs (5322, 5321, 6531) without regex. Message composition with proper header ordering. International email support built in.

**HTTP Standards** - Content-Type parsing, Content-Disposition handling, multipart messages, cookies. All the HTTP building blocks with types instead of strings.

**Form Data** - Hierarchical form data structures that parse and encode with multiple strategies. File uploads with proper MIME types. No more manual string manipulation.

**Authentication** - JWT parsing and validation, TOTP for two-factor auth, OAuth bearer tokens, Basic authentication. Security primitives without the security vulnerabilities.

**Domain Names** - Multi-RFC domain validation that automatically detects which standards apply. Subdomain operations that can't create invalid domains.

**And More** - Feed formats (Atom, RSS, JSON Feed), mailing list headers, WHATWG standards for modern web compatibility.

34 packages total. Each production-ready, extensively tested, fully documented. Zero dependencies where possible. Swift 6.0 strict concurrency throughout.

## What This Approach Enables

**Catch Errors at Compile Time** - Invalid URLs, malformed emails, incorrect header formats—all caught before your code runs. Not with linters or analyzers, but with Swift's type system doing what it does best.

**Composable Primitives** - Small, focused packages that work together. Email addresses compose with SMTP types. URI templates compose with HTTP routing. Domain validation composes with email validation. Build complex systems from simple, correct parts.

**Framework Independence** - These aren't tied to Vapor, Hummingbird, or any specific framework. They're foundation layers that any server-side Swift project can build on. Implement a standard once, use it everywhere.

**Production Confidence** - When your types guarantee RFC compliance, you don't write defensive code checking for edge cases. You write straightforward code that the compiler proves correct.

**Better APIs** - Type-safe primitives enable better framework APIs. Routing can use URI templates with compile-time variable validation. Email libraries can guarantee valid addresses. Form handlers can work with structured data instead of string dictionaries.

## Philosophy

We believe Swift deserves implementations that are:
- **Correct** - Full RFC compliance, not "good enough"
- **Safe** - Compile-time guarantees eliminate entire classes of errors
- **Fast** - Zero runtime overhead, optimal performance
- **Modern** - Swift 6.0 concurrency, latest language features
- **Composable** - Small, focused packages that work together

The web's foundation shouldn't require runtime validation. Type-safe primitives make wrong things impossible and right things obvious.

## Impact

These packages power production systems:
- **[coenttb-com-server](https://github.com/coenttb/coenttb-com-server)** - 100% Swift website, type-safe from database to DOM
- **[swift-html](https://github.com/coenttb/swift-html)** - Type-safe HTML generation
- **[swift-identities](https://github.com/coenttb/swift-identities)** - Complete authentication system
- Server-side Swift applications across email, forms, and routing

By implementing standards correctly once, we enable entire ecosystems to build with confidence.

## Vision

Swift has proven itself on Apple platforms. Server-side Swift is proving itself in production. But the web's foundation—URL parsing, email validation, HTTP handling—remains fragmented across frameworks.

We're building the standard library Swift's web ecosystem deserves. Type-safe primitives that make it impossible to generate invalid URLs, impossible to create malformed emails, impossible to parse data incorrectly.

Every RFC implementation removes complexity from every framework built on top. Every type-safe abstraction prevents errors before they happen. Every package proves Swift belongs on the server.

**The web runs on standards. Those standards should run on types.**

## Get Involved

Browse our repositories to see implementations of specific RFCs. Each package is independently useful and designed to compose with others.

All packages are Apache 2.0 licensed—maximum compatibility for both open source and commercial projects.

---

*Founded by [Coen ten Thije Boonkkamp](https://github.com/coenttb) • Building in public • One RFC at a time*
