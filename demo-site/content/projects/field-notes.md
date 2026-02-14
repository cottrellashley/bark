---
title: "Field Notes"
tags: [ios, swift]
description: "A minimal note-taking app for field research. Captures text, GPS coordinates, and photos with offline-first sync."
---

# Field Notes

A mobile app designed for researchers and naturalists who need to capture observations in the field, even without connectivity.

## Design Principles

1. **Offline-first** — everything works without a network connection
2. **Fast capture** — one tap to start a new note
3. **Structured data** — GPS, timestamp, weather, and custom fields attached automatically
4. **Sync when ready** — changes merge cleanly when connectivity returns

## Architecture

- SwiftUI frontend
- Core Data for local persistence
- CloudKit for sync
- MapKit for location display
