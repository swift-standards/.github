# Swift Standards

Type-safe implementations of internet standards (RFCs) as Swift packages.

## Overview

Swift Standards provides RFC-compliant implementations of web protocols and data formats. Each package implements a specific internet standard with Swift's type system, enabling compile-time validation instead of runtime string parsing.

The packages cover URI handling, email formats, HTTP headers, form data, authentication protocols, and syndication feeds. All packages use Swift 6.0 strict concurrency and maintain zero dependencies where possible.

## Implementation Areas

**URI Standard**
RFC 3986 (URI syntax), RFC 3987 (internationalized URIs), RFC 6570 (URI templates). Full parsing, manipulation, and template expansion with compile-time variable validation.

**Email Standards**
RFC 5322 (message format), RFC 5321 (SMTP), RFC 6531 (internationalized email). Address validation across multiple RFC formats, message composition, header management.

**HTTP Standards**
RFC 7230/7231 (HTTP/1.1), RFC 2045/2046 (MIME), RFC 2183 (Content-Disposition), RFC 6265 (cookies). Header parsing, content type handling, multipart messages.

**Form Data**
RFC 2388/7578 (multipart form data), WHATWG URL encoding. Hierarchical data structures with multiple parsing strategies, file upload handling.

**Authentication**
RFC 7519 (JWT), RFC 6238 (TOTP), RFC 6750 (OAuth Bearer), RFC 7617 (Basic Auth). Token validation, two-factor authentication, credential handling.

**Domain standards**
RFC 1035 (DNS), RFC 1123 (hostnames), RFC 5321 (SMTP domains). Multi-RFC validation with automatic format detection, subdomain operations.

**Syndication**
RFC 4287 (Atom), RSS 2.0, JSON Feed. Feed parsing and generation with type-safe structures.

34 total packages. Each independently tested and documented.

## Technical Approach

All implementations use Swift's type system for validation. Invalid data structures are rejected at compile time rather than runtime. Types compose across packages—email addresses work with SMTP types, URI templates integrate with routing systems, domain validation combines with email validation.

Packages are framework-independent. Each package focuses on a single standard with minimal dependencies.

## Requirements

- Swift 6.0+
- macOS 13.0+ / iOS 16.0+ / Linux

## License

All packages use Apache License 2.0.
