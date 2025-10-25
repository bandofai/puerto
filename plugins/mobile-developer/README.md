# Mobile Developer Plugin

Mobile app development specialist for iOS/Android applications, mobile UI/UX implementation, platform-specific optimization, performance tuning, and app store preparation.

## Overview

The Mobile Developer plugin provides agents for building native and cross-platform mobile applications using Swift/SwiftUI, Kotlin/Jetpack Compose, React Native, and Flutter with platform-specific best practices.

## Agents

### 1. ios-developer (Sonnet, Skill-Aware)
Develops iOS applications using Swift, SwiftUI, UIKit, and iOS-specific frameworks.

**Use for**: iOS app development, SwiftUI interfaces, iOS SDK integration, App Store preparation

**Example**:
```
Use ios-developer to create iOS app for fitness tracking.
Requirements:
- SwiftUI interface with tab navigation
- HealthKit integration for step counting
- Core Data for workout history
- Push notifications for reminders
- Dark mode support
- iOS 15+ target
Include: Architecture (MVVM), async/await patterns, SwiftUI best practices
```

### 2. android-developer (Sonnet, Skill-Aware)
Develops Android applications using Kotlin, Jetpack Compose, and Android SDK.

**Use for**: Android app development, Jetpack Compose UI, Android SDK integration, Play Store preparation

**Example**:
```
Use android-developer to create Android companion for fitness app.
Requirements:
- Jetpack Compose UI with Material 3
- Google Fit API integration
- Room database for local storage
- WorkManager for background sync
- Notification channels
- Target API 33 (Android 13)
Include: Architecture (MVVM/Clean), Kotlin coroutines, Compose best practices
```

### 3. mobile-ui-designer (Sonnet, Skill-Aware)
Implements mobile-first UI/UX with platform-specific design guidelines (HIG for iOS, Material for Android).

**Use for**: Mobile UI implementation, responsive layouts, gesture handling, accessibility, platform conventions

**Example**:
```
Use mobile-ui-designer for e-commerce mobile app UI.
Platforms: iOS and Android
Screens: Product listing, detail, cart, checkout
Design system: Custom brand colors with platform conventions
Requirements:
- Bottom tab navigation (iOS) / Bottom nav bar (Android)
- Pull-to-refresh
- Swipe gestures for favorites
- Skeleton screens for loading
- Adaptive layouts (phone/tablet)
- Accessibility (VoiceOver/TalkBack)
```

### 4. performance-optimizer (Sonnet, Skill-Aware)
Optimizes mobile app performance: launch time, memory usage, battery efficiency, network efficiency.

**Use for**: Performance profiling, optimization, memory leaks, battery usage, app size reduction

**Example**:
```
Use performance-optimizer to improve app performance.
Issues:
- Slow app launch (5 seconds)
- High memory usage causing crashes
- Excessive battery drain
- 100MB app size
Analysis:
- Profile launch sequence and identify bottlenecks
- Find memory leaks and retain cycles
- Optimize network calls (batching, caching)
- Reduce binary size (remove unused assets, compress images)
- Background task optimization
```

## Skills

### mobile-development
Platform-specific development patterns and best practices:
- **iOS**: Swift, SwiftUI, UIKit, Combine, async/await, Core Data, HealthKit, ARKit
- **Android**: Kotlin, Jetpack Compose, ViewModel, LiveData/Flow, Room, WorkManager
- **Cross-platform**: React Native, Flutter/Dart, shared business logic
- **Architecture**: MVVM, Clean Architecture, MVI, Redux
- **State Management**: SwiftUI State, Jetpack Compose State, Redux/MobX
- **Networking**: URLSession, Retrofit, REST/GraphQL clients
- **Storage**: Core Data, Room, SQLite, UserDefaults/SharedPreferences
- **Testing**: XCTest, JUnit, UI testing, snapshot testing

### mobile-ux
Mobile-specific UX patterns and platform conventions:
- **iOS HIG**: Human Interface Guidelines, navigation patterns, iOS controls
- **Material Design**: Material 3, Android components, motion design
- **Touch Targets**: 44pt (iOS) / 48dp (Android) minimum
- **Navigation**: Tab bars, navigation bars, bottom sheets, modals
- **Gestures**: Swipe, pinch, long-press, edge swipes
- **Responsive**: Phone, tablet, landscape, split-screen
- **Accessibility**: VoiceOver, TalkBack, Dynamic Type, color contrast
- **Offline**: Offline-first design, sync strategies, error states

## Templates

### ios-app-template.md
Complete iOS app structure: SwiftUI views, MVVM architecture, Core Data models, networking layer, dependency injection, unit tests, UI tests.

### android-app-template.md
Complete Android app structure: Jetpack Compose UI, ViewModel + Repository pattern, Room database, Retrofit networking, Hilt DI, tests.

### mobile-ui-patterns.md
Platform-specific UI patterns: Navigation (iOS vs Android), lists, forms, loading states, empty states, error handling, pull-to-refresh, infinite scroll.

### app-performance-checklist.md
Performance optimization checklist: Launch time, memory management, battery usage, network efficiency, app size, rendering performance, background tasks.

## Workflows

### Complete Mobile App Development
```
1. iOS implementation
Use ios-developer to build iOS version with SwiftUI

2. Android implementation
Use android-developer to build Android version with Jetpack Compose

3. Mobile UI/UX
Use mobile-ui-designer to implement platform-specific UI patterns

4. Performance optimization
Use performance-optimizer to profile and optimize both platforms
```

### Cross-Platform App
```
Option 1: React Native
Use ios-developer and android-developer for React Native setup
Use mobile-ui-designer for platform-specific UI components
Use performance-optimizer for RN-specific optimizations

Option 2: Flutter
Use mobile-ui-designer for Flutter/Dart UI implementation
Use performance-optimizer for Flutter performance tuning
```

## Requirements Met

✅ Role: Mobile app development specialist
✅ Mobile app development: ios-developer and android-developer for native platforms
✅ Platform-specific optimization: Agents follow iOS HIG and Material Design
✅ Mobile UI/UX implementation: mobile-ui-designer with platform conventions
✅ Performance optimization: performance-optimizer for launch time, memory, battery
✅ App store optimization: Covered in templates and app preparation guidance
✅ Tools: Code execution (Bash), mobile SDKs (guidance), file operations

## Key Features

✓ **Native iOS**: Swift, SwiftUI, iOS 15+ features
✓ **Native Android**: Kotlin, Jetpack Compose, Material 3
✓ **Cross-Platform**: React Native, Flutter support
✓ **Modern Architecture**: MVVM, Clean Architecture patterns
✓ **Platform Conventions**: iOS HIG, Material Design compliance
✓ **Performance**: Launch time, memory, battery optimization
✓ **Accessibility**: VoiceOver, TalkBack, Dynamic Type
✓ **Offline-First**: Local storage, sync strategies

## Platform-Specific Patterns

### iOS Best Practices
- SwiftUI for UI (iOS 15+) or UIKit for older versions
- Combine or async/await for reactive programming
- Core Data or SwiftData for persistence
- URLSession for networking
- Push notifications via APNs
- In-app purchases via StoreKit
- App Clips, Widgets, Live Activities

### Android Best Practices
- Jetpack Compose for UI (Material 3)
- ViewModel + Repository pattern
- Room for database, DataStore for preferences
- Retrofit + OkHttp for networking
- WorkManager for background tasks
- Firebase Cloud Messaging for push
- In-app purchases via Play Billing
- App Bundles for optimized distribution

## Performance Targets

- **Launch time**: < 2 seconds (cold start)
- **Memory**: < 100MB typical, < 200MB peak
- **Battery**: < 5% drain per hour active use
- **App size**: < 50MB compressed (ideal), < 100MB max
- **Frame rate**: 60 FPS (iOS/Android), 120 FPS (ProMotion)
- **API response**: < 200ms perceived (loading states)

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 2 comprehensive skills (mobile-development, mobile-ux)
- ✅ 4 professional templates for iOS, Android, UI, and performance
- ✅ Complete README with platform-specific workflows

Closes #76
