# Mobile UX Skill

Comprehensive mobile user experience design principles, platform-specific guidelines (iOS Human Interface Guidelines, Material Design 3), mobile interaction patterns, accessibility, and responsive design for building intuitive mobile interfaces.

## Overview

This skill covers iOS Human Interface Guidelines, Material Design 3, mobile-specific interaction patterns, touch targets and gestures, mobile navigation patterns, responsive layouts, accessibility (VoiceOver, TalkBack), and platform conventions.

## iOS Human Interface Guidelines (HIG)

### Core iOS Design Principles

**Clarity**:
- Text is legible at every size
- Icons are precise and lucid
- Adornments are subtle and appropriate
- Functionality is sharpened through design

**Deference**:
- Fluid motion and crisp interface help people understand and interact with content
- Content typically fills entire screen
- Translucency and blurring often hint at more

**Depth**:
- Visual layers and realistic motion convey hierarchy
- Touch and discoverability heighten delight
- Transitions provide sense of depth

### iOS Typography

**SF Pro (System Font)**:
```swift
// Font weights
let largeTitle = UIFont.preferredFont(forTextStyle: .largeTitle) // 34pt
let title1 = UIFont.preferredFont(forTextStyle: .title1)         // 28pt
let title2 = UIFont.preferredFont(forTextStyle: .title2)         // 22pt
let title3 = UIFont.preferredFont(forTextStyle: .title3)         // 20pt
let headline = UIFont.preferredFont(forTextStyle: .headline)     // 17pt semibold
let body = UIFont.preferredFont(forTextStyle: .body)             // 17pt regular
let callout = UIFont.preferredFont(forTextStyle: .callout)       // 16pt
let subheadline = UIFont.preferredFont(forTextStyle: .subheadline) // 15pt
let footnote = UIFont.preferredFont(forTextStyle: .footnote)     // 13pt
let caption1 = UIFont.preferredFont(forTextStyle: .caption1)     // 12pt
let caption2 = UIFont.preferredFont(forTextStyle: .caption2)     // 11pt

// SwiftUI
Text("Title")
    .font(.largeTitle)
    .fontWeight(.bold)
```

**Dynamic Type Support**:
- Always use text styles, not fixed sizes
- Test with accessibility sizes (Settings > Accessibility > Display & Text Size > Larger Text)
- Content should remain readable at largest sizes

### iOS Color System

**System Colors** (adapt to dark mode automatically):
```swift
// Primary colors
UIColor.label                    // Primary text
UIColor.secondaryLabel           // Secondary text
UIColor.tertiaryLabel           // Tertiary text
UIColor.quaternaryLabel         // Watermark text

// Background colors
UIColor.systemBackground         // Primary background
UIColor.secondarySystemBackground // Content background
UIColor.tertiarySystemBackground // Grouped content background

// Fill colors (for UI elements)
UIColor.systemFill
UIColor.secondarySystemFill
UIColor.tertiarySystemFill
UIColor.quaternarySystemFill

// Tint colors
UIColor.systemBlue
UIColor.systemGreen
UIColor.systemRed
UIColor.systemOrange
UIColor.systemYellow
UIColor.systemPink
UIColor.systemPurple
UIColor.systemTeal
UIColor.systemIndigo
```

**Color Contrast**:
- 4.5:1 minimum for normal text
- 3:1 minimum for large text (18pt+)
- Test in both light and dark mode

### iOS Spacing & Layout

**Safe Area**:
```swift
// Respect safe area insets
view.safeAreaLayoutGuide

// SwiftUI
VStack {
    // Content
}
.safeAreaInset(edge: .bottom) {
    // Toolbar
}
```

**Standard Spacing**:
- 8pt grid system
- Minimum touch target: 44x44pt (iOS standard)
- Edge margins: 16-20pt
- Component spacing: 8pt, 16pt, 24pt

**Layout Margins**:
```swift
// UIKit
view.layoutMargins = UIEdgeInsets(top: 8, left: 16, bottom: 8, right: 16)
view.directionalLayoutMargins = NSDirectionalEdgeInsets(
    top: 8, leading: 16, bottom: 8, trailing: 16
)

// SwiftUI
VStack {
    Text("Content")
}
.padding(.horizontal, 16)
```

### iOS Navigation Patterns

**Navigation Bar**:
```swift
// Large title (default, scrolls to inline)
navigationController?.navigationBar.prefersLargeTitles = true
navigationItem.largeTitleDisplayMode = .automatic

// Navigation items
navigationItem.title = "Settings"
navigationItem.rightBarButtonItem = UIBarButtonItem(
    barButtonSystemItem: .add,
    target: self,
    action: #selector(addTapped)
)

// SwiftUI
NavigationStack {
    ListView()
        .navigationTitle("Items")
        .navigationBarTitleDisplayMode(.large)
        .toolbar {
            ToolbarItem(placement: .navigationBarTrailing) {
                Button("Add") { }
            }
        }
}
```

**Tab Bar**:
```swift
// UIKit
let tabBarController = UITabBarController()
tabBarController.viewControllers = [
    UINavigationController(rootViewController: HomeViewController()),
    UINavigationController(rootViewController: SearchViewController()),
    UINavigationController(rootViewController: ProfileViewController())
]

// SwiftUI
TabView {
    HomeView()
        .tabItem {
            Label("Home", systemImage: "house")
        }
    SearchView()
        .tabItem {
            Label("Search", systemImage: "magnifyingglass")
        }
    ProfileView()
        .tabItem {
            Label("Profile", systemImage: "person")
        }
}
```

**Modal Presentation**:
```swift
// Sheet (default)
present(viewController, animated: true)

// Full screen
viewController.modalPresentationStyle = .fullScreen
present(viewController, animated: true)

// SwiftUI
.sheet(isPresented: $showingSheet) {
    DetailView()
}

.fullScreenCover(isPresented: $showingFullScreen) {
    OnboardingView()
}
```

### iOS UI Components

**Buttons**:
```swift
// SwiftUI button styles
Button("Primary") { }
    .buttonStyle(.borderedProminent)

Button("Secondary") { }
    .buttonStyle(.bordered)

Button("Plain") { }
    .buttonStyle(.plain)

// SF Symbols in buttons
Button {
    // Action
} label: {
    Label("Share", systemImage: "square.and.arrow.up")
}
```

**Lists**:
```swift
// SwiftUI list styles
List {
    ForEach(items) { item in
        Text(item.name)
    }
}
.listStyle(.insetGrouped)  // Grouped style
.listStyle(.plain)         // Plain style
.listStyle(.sidebar)       // Sidebar style
```

**Forms**:
```swift
Form {
    Section {
        TextField("Name", text: $name)
        TextField("Email", text: $email)
            .keyboardType(.emailAddress)
            .textContentType(.emailAddress)
    }

    Section {
        Toggle("Notifications", isOn: $notificationsEnabled)
        Picker("Theme", selection: $theme) {
            Text("Light").tag(Theme.light)
            Text("Dark").tag(Theme.dark)
            Text("System").tag(Theme.system)
        }
    }
}
```

### iOS Gestures

**Standard Gestures**:
- **Tap**: Select, activate
- **Drag**: Scroll, pan, swipe
- **Flick**: Scroll quickly
- **Swipe**: Reveal actions, navigate
- **Double tap**: Zoom in/out
- **Pinch**: Zoom in/out
- **Long press**: Context menu, edit mode
- **Rotate**: Rotate content

```swift
// SwiftUI gestures
Image("photo")
    .gesture(
        MagnificationGesture()
            .onChanged { value in
                scale = value
            }
    )
    .gesture(
        RotationGesture()
            .onChanged { angle in
                rotation = angle
            }
    )

// Context menu
Text("Item")
    .contextMenu {
        Button("Copy") { }
        Button("Share") { }
        Button("Delete", role: .destructive) { }
    }
```

### iOS Dark Mode

```swift
// Automatic dark mode support
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    super.traitCollectionDidChange(previousTraitCollection)

    if traitCollection.hasDifferentColorAppearance(comparedTo: previousTraitCollection) {
        // Update custom colors
    }
}

// SwiftUI
@Environment(\.colorScheme) var colorScheme

Color(colorScheme == .dark ? .white : .black)

// Asset catalog colors (automatically adapt)
Color("CustomColor") // Define in Assets.xcassets with light/dark variants
```

## Material Design 3 (Material You)

### Material Design Principles

**Adaptive**:
- Personalized with dynamic color
- Accessible by default
- Responsive to context

**Expressive**:
- Bold, large typography
- High contrast color schemes
- Purposeful motion

**Coherent**:
- Unified system across platforms
- Consistent patterns
- Clear hierarchy

### Material Design 3 Color System

**Dynamic Color**:
```kotlin
// Material Theme Builder generated colors
val LightColors = lightColorScheme(
    primary = md_theme_light_primary,
    onPrimary = md_theme_light_onPrimary,
    primaryContainer = md_theme_light_primaryContainer,
    onPrimaryContainer = md_theme_light_onPrimaryContainer,
    secondary = md_theme_light_secondary,
    // ... more colors
)

val DarkColors = darkColorScheme(
    primary = md_theme_dark_primary,
    onPrimary = md_theme_dark_onPrimary,
    // ... more colors
)

// Apply theme
@Composable
fun MyAppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colorScheme = if (darkTheme) DarkColors else LightColors

    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        shapes = Shapes,
        content = content
    )
}
```

**Color Roles**:
- **Primary**: Main brand color, key components
- **Secondary**: Less prominent components
- **Tertiary**: Accents, contrasting elements
- **Error**: Error states
- **Surface**: Background surfaces
- **On[Color]**: Text/icons on that color

### Material Typography

**Type Scale**:
```kotlin
val Typography = Typography(
    displayLarge = TextStyle(fontSize = 57.sp, lineHeight = 64.sp),
    displayMedium = TextStyle(fontSize = 45.sp, lineHeight = 52.sp),
    displaySmall = TextStyle(fontSize = 36.sp, lineHeight = 44.sp),

    headlineLarge = TextStyle(fontSize = 32.sp, lineHeight = 40.sp),
    headlineMedium = TextStyle(fontSize = 28.sp, lineHeight = 36.sp),
    headlineSmall = TextStyle(fontSize = 24.sp, lineHeight = 32.sp),

    titleLarge = TextStyle(fontSize = 22.sp, lineHeight = 28.sp),
    titleMedium = TextStyle(fontSize = 16.sp, lineHeight = 24.sp, fontWeight = FontWeight.Medium),
    titleSmall = TextStyle(fontSize = 14.sp, lineHeight = 20.sp, fontWeight = FontWeight.Medium),

    bodyLarge = TextStyle(fontSize = 16.sp, lineHeight = 24.sp),
    bodyMedium = TextStyle(fontSize = 14.sp, lineHeight = 20.sp),
    bodySmall = TextStyle(fontSize = 12.sp, lineHeight = 16.sp),

    labelLarge = TextStyle(fontSize = 14.sp, lineHeight = 20.sp, fontWeight = FontWeight.Medium),
    labelMedium = TextStyle(fontSize = 12.sp, lineHeight = 16.sp, fontWeight = FontWeight.Medium),
    labelSmall = TextStyle(fontSize = 11.sp, lineHeight = 16.sp, fontWeight = FontWeight.Medium)
)

// Usage
Text(
    text = "Headline",
    style = MaterialTheme.typography.headlineMedium
)
```

### Material Spacing

**Standard Spacing** (4dp grid):
```kotlin
// Common spacing values
4.dp, 8.dp, 12.dp, 16.dp, 24.dp, 32.dp, 48.dp

// Minimum touch target: 48x48dp (Android standard)

// Usage
Column(
    modifier = Modifier.padding(16.dp),
    verticalArrangement = Arrangement.spacedBy(8.dp)
) {
    // Content
}
```

### Material Components

**Buttons**:
```kotlin
// Filled button (high emphasis)
Button(onClick = { }) {
    Text("Filled Button")
}

// Outlined button (medium emphasis)
OutlinedButton(onClick = { }) {
    Text("Outlined Button")
}

// Text button (low emphasis)
TextButton(onClick = { }) {
    Text("Text Button")
}

// Icon button
IconButton(onClick = { }) {
    Icon(Icons.Default.Favorite, contentDescription = "Favorite")
}

// FAB (Floating Action Button)
FloatingActionButton(
    onClick = { },
    containerColor = MaterialTheme.colorScheme.primaryContainer
) {
    Icon(Icons.Default.Add, contentDescription = "Add")
}
```

**Cards**:
```kotlin
// Elevated card
Card(
    modifier = Modifier
        .fillMaxWidth()
        .padding(16.dp),
    elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)
) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Title", style = MaterialTheme.typography.titleLarge)
        Spacer(modifier = Modifier.height(8.dp))
        Text("Content", style = MaterialTheme.typography.bodyMedium)
    }
}

// Filled card
Card(
    modifier = Modifier.fillMaxWidth(),
    colors = CardDefaults.cardColors(
        containerColor = MaterialTheme.colorScheme.surfaceVariant
    )
) {
    // Content
}

// Outlined card
OutlinedCard(modifier = Modifier.fillMaxWidth()) {
    // Content
}
```

**Navigation**:
```kotlin
// Bottom navigation bar
NavigationBar {
    items.forEachIndexed { index, item ->
        NavigationBarItem(
            icon = { Icon(item.icon, contentDescription = item.label) },
            label = { Text(item.label) },
            selected = selectedIndex == index,
            onClick = { selectedIndex = index }
        )
    }
}

// Navigation rail (tablet/desktop)
NavigationRail {
    items.forEach { item ->
        NavigationRailItem(
            icon = { Icon(item.icon, contentDescription = item.label) },
            label = { Text(item.label) },
            selected = selectedItem == item,
            onClick = { selectedItem = item }
        )
    }
}

// Navigation drawer
ModalNavigationDrawer(
    drawerState = drawerState,
    drawerContent = {
        ModalDrawerSheet {
            items.forEach { item ->
                NavigationDrawerItem(
                    label = { Text(item.label) },
                    selected = selectedItem == item,
                    onClick = { selectedItem = item }
                )
            }
        }
    }
) {
    // Main content
}
```

**Top app bar**:
```kotlin
// Small top app bar
TopAppBar(
    title = { Text("Title") },
    navigationIcon = {
        IconButton(onClick = { }) {
            Icon(Icons.Default.Menu, contentDescription = "Menu")
        }
    },
    actions = {
        IconButton(onClick = { }) {
            Icon(Icons.Default.Search, contentDescription = "Search")
        }
    }
)

// Medium top app bar (scrolls)
MediumTopAppBar(
    title = { Text("Title") },
    scrollBehavior = TopAppBarDefaults.exitUntilCollapsedScrollBehavior()
)

// Large top app bar
LargeTopAppBar(
    title = { Text("Title") }
)
```

**Dialogs**:
```kotlin
AlertDialog(
    onDismissRequest = { },
    title = { Text("Dialog Title") },
    text = { Text("Dialog message goes here") },
    confirmButton = {
        TextButton(onClick = { }) {
            Text("Confirm")
        }
    },
    dismissButton = {
        TextButton(onClick = { }) {
            Text("Cancel")
        }
    }
)
```

### Material Motion

**Standard Easing Curves**:
```kotlin
// Emphasized easing (Material 3 default)
val emphasizedEasing = CubicBezierEasing(0.2f, 0f, 0f, 1f)

// Standard easing
val standardEasing = CubicBezierEasing(0.4f, 0f, 0.2f, 1f)

// Decelerate easing (enter)
val decelerateEasing = CubicBezierEasing(0f, 0f, 0.2f, 1f)

// Accelerate easing (exit)
val accelerateEasing = CubicBezierEasing(0.4f, 0f, 1f, 1f)

// Standard durations
val shortDuration = 200.milliseconds
val mediumDuration = 300.milliseconds
val longDuration = 400.milliseconds
```

**Transitions**:
```kotlin
// Fade transition
AnimatedVisibility(
    visible = isVisible,
    enter = fadeIn(animationSpec = tween(300)),
    exit = fadeOut(animationSpec = tween(300))
) {
    // Content
}

// Slide transition
AnimatedVisibility(
    visible = isVisible,
    enter = slideInVertically() + fadeIn(),
    exit = slideOutVertically() + fadeOut()
) {
    // Content
}

// Expand/collapse
AnimatedVisibility(
    visible = expanded,
    enter = expandVertically() + fadeIn(),
    exit = shrinkVertically() + fadeOut()
) {
    // Content
}
```

## Touch Targets & Gestures

### Minimum Touch Target Sizes

**iOS**: 44x44 points
**Android**: 48x48 dp (density-independent pixels)

```swift
// iOS - extend touch area if visual element is smaller
Button {
    Image(systemName: "xmark")
        .font(.system(size: 16))
} label: {
    // Visual size: 16x16
    // Touch area: 44x44 (extended automatically)
}
.frame(width: 44, height: 44)
```

```kotlin
// Android - ensure minimum touch target
IconButton(
    onClick = { },
    modifier = Modifier.size(48.dp) // Minimum touch target
) {
    Icon(
        imageVector = Icons.Default.Close,
        contentDescription = "Close",
        modifier = Modifier.size(24.dp) // Visual size
    )
}
```

### Common Gestures

**Tap/Click**:
- Primary action
- Selection
- Toggle

**Long Press**:
- Context menu (iOS)
- Selection mode (Android)
- Additional options

**Swipe**:
- Navigate between screens
- Reveal actions (swipe on list item)
- Dismiss

```swift
// iOS swipe actions
List {
    ForEach(items) { item in
        Text(item.name)
            .swipeActions(edge: .trailing) {
                Button(role: .destructive) {
                    delete(item)
                } label: {
                    Label("Delete", systemImage: "trash")
                }

                Button {
                    archive(item)
                } label: {
                    Label("Archive", systemImage: "archivebox")
                }
                .tint(.blue)
            }
    }
}
```

```kotlin
// Android swipe to dismiss
SwipeToDismiss(
    state = dismissState,
    background = {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(Color.Red)
                .padding(16.dp),
            contentAlignment = Alignment.CenterEnd
        ) {
            Icon(Icons.Default.Delete, contentDescription = "Delete")
        }
    },
    dismissContent = {
        Card {
            Text("Swipe to delete")
        }
    }
)
```

**Pull to Refresh**:
```swift
// iOS
List(items) { item in
    Text(item.name)
}
.refreshable {
    await refresh()
}
```

```kotlin
// Android
val pullRefreshState = rememberPullRefreshState(
    refreshing = isRefreshing,
    onRefresh = { refresh() }
)

Box(modifier = Modifier.pullRefresh(pullRefreshState)) {
    LazyColumn {
        items(items) { item ->
            Text(item.name)
        }
    }

    PullRefreshIndicator(
        refreshing = isRefreshing,
        state = pullRefreshState,
        modifier = Modifier.align(Alignment.TopCenter)
    )
}
```

## Mobile Navigation Patterns

### Tab Navigation

**When to use**:
- 3-5 top-level destinations
- Equal importance
- Frequent switching

**iOS Tab Bar**:
- Bottom placement
- 44pt height
- Icons + labels (optional)
- Max 5 tabs (more → "More" tab)

**Android Bottom Navigation**:
- Bottom placement
- 56dp height
- Icons + labels
- 3-5 items recommended

### Stack Navigation

**When to use**:
- Hierarchical content
- Linear flow
- Drill-down pattern

**iOS Navigation Stack**:
- Navigation bar at top
- Back button (automatic)
- Large title (optional)

**Android Up Navigation**:
- App bar at top
- Up/back arrow
- Handles back stack

### Drawer Navigation

**When to use**:
- 5+ top-level destinations
- Secondary navigation
- Settings, profile access

**iOS**: Less common (prefer tab bar or list)
**Android**: Standard pattern (slide from left edge)

```kotlin
// Android navigation drawer
ModalNavigationDrawer(
    drawerState = drawerState,
    drawerContent = {
        ModalDrawerSheet {
            // Header
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(160.dp)
                    .background(MaterialTheme.colorScheme.primary)
            ) {
                // User info
            }

            // Navigation items
            Divider()
            NavigationDrawerItem(
                label = { Text("Home") },
                selected = false,
                onClick = { }
            )
        }
    }
) {
    // Main content
}
```

## Responsive Layouts

### iOS Size Classes

**Horizontal Size Classes**:
- **Compact**: iPhone portrait, iPhone landscape (smaller devices)
- **Regular**: iPad portrait/landscape, iPhone Plus landscape

**Vertical Size Classes**:
- **Compact**: iPhone landscape
- **Regular**: iPhone portrait, iPad portrait/landscape

```swift
@Environment(\.horizontalSizeClass) var horizontalSizeClass

var body: some View {
    if horizontalSizeClass == .compact {
        // Phone layout (stack)
        VStack {
            SidebarView()
            ContentView()
        }
    } else {
        // Tablet/desktop layout (side-by-side)
        HStack {
            SidebarView()
            ContentView()
        }
    }
}
```

### Android Window Size Classes

**Width Classes**:
- **Compact**: < 600dp (phone portrait)
- **Medium**: 600-840dp (tablet portrait, phone landscape)
- **Expanded**: > 840dp (tablet landscape, desktop)

**Height Classes**:
- **Compact**: < 480dp (phone landscape)
- **Medium**: 480-900dp (phone portrait, tablet portrait)
- **Expanded**: > 900dp (tablet landscape)

```kotlin
@Composable
fun AdaptiveLayout() {
    val windowSizeClass = calculateWindowSizeClass()

    when (windowSizeClass.widthSizeClass) {
        WindowWidthSizeClass.Compact -> {
            // Phone layout - single pane
            Column {
                TopBar()
                ContentList()
                BottomNavigation()
            }
        }

        WindowWidthSizeClass.Medium -> {
            // Tablet portrait - navigation rail
            Row {
                NavigationRail()
                ContentList()
            }
        }

        WindowWidthSizeClass.Expanded -> {
            // Tablet landscape / desktop - drawer + detail
            Row {
                PermanentNavigationDrawer()
                ContentList()
                DetailPane()
            }
        }
    }
}
```

### Multi-pane Layouts

**List-Detail (Master-Detail)**:
```swift
// iOS
NavigationSplitView {
    // List
    List(items) { item in
        NavigationLink(value: item) {
            Text(item.name)
        }
    }
} detail: {
    // Detail
    if let selectedItem {
        DetailView(item: selectedItem)
    } else {
        Text("Select an item")
    }
}
```

```kotlin
// Android
ListDetailPaneScaffold(
    listPane = {
        LazyColumn {
            items(items) { item ->
                ListItem(
                    headlineContent = { Text(item.name) },
                    modifier = Modifier.clickable { selectedItem = item }
                )
            }
        }
    },
    detailPane = {
        selectedItem?.let { item ->
            DetailView(item = item)
        } ?: Text("Select an item")
    }
)
```

## Accessibility

### iOS Accessibility (VoiceOver)

**Basic Accessibility**:
```swift
// UIKit
button.accessibilityLabel = "Add to cart"
button.accessibilityHint = "Adds this item to your shopping cart"
button.accessibilityTraits = .button

imageView.isAccessibilityElement = true
imageView.accessibilityLabel = "Product photo"

// SwiftUI
Button("Add") { }
    .accessibilityLabel("Add to cart")
    .accessibilityHint("Adds this item to your shopping cart")

Image("product")
    .accessibilityLabel("Product photo")
    .accessibilityHidden(isDecorative)
```

**Custom Actions**:
```swift
// Custom VoiceOver actions
view.accessibilityCustomActions = [
    UIAccessibilityCustomAction(name: "Delete") { _ in
        delete()
        return true
    },
    UIAccessibilityCustomAction(name: "Share") { _ in
        share()
        return true
    }
]
```

**Grouping Elements**:
```swift
containerView.isAccessibilityElement = true
containerView.accessibilityLabel = "Product: iPhone 14 Pro, Price: $999"
// VoiceOver reads as single element instead of multiple
```

**Dynamic Type**:
```swift
// Support larger text sizes
label.font = UIFont.preferredFont(forTextStyle: .body)
label.adjustsFontForContentSizeCategory = true

// SwiftUI
Text("Content")
    .font(.body)
    .dynamicTypeSize(.medium...DynamicTypeSize.accessibility5)
```

### Android Accessibility (TalkBack)

**Content Descriptions**:
```kotlin
// Basic accessibility
Button(onClick = { }) {
    Icon(
        imageVector = Icons.Default.Add,
        contentDescription = "Add to cart"
    )
}

Image(
    painter = painterResource(R.drawable.product),
    contentDescription = "Product photo"
)

// Decorative images (no announcement)
Image(
    painter = painterResource(R.drawable.decoration),
    contentDescription = null // Explicitly null for decorative
)
```

**Semantic Properties**:
```kotlin
Text(
    text = "Important heading",
    modifier = Modifier.semantics {
        heading()
    }
)

Checkbox(
    checked = isChecked,
    onCheckedChange = { isChecked = it },
    modifier = Modifier.semantics {
        contentDescription = "Subscribe to newsletter"
        stateDescription = if (isChecked) "Subscribed" else "Not subscribed"
    }
)
```

**Custom Actions**:
```kotlin
Card(
    modifier = Modifier
        .fillMaxWidth()
        .clickable { viewDetails() }
        .semantics {
            customActions = listOf(
                CustomAccessibilityAction("Delete") {
                    delete()
                    true
                },
                CustomAccessibilityAction("Share") {
                    share()
                    true
                }
            )
        }
) {
    // Content
}
```

**Grouping Elements**:
```kotlin
Row(
    modifier = Modifier.semantics(mergeDescendants = true) {
        contentDescription = "Product: iPhone 14 Pro, Price: 999 dollars"
    }
) {
    Text("iPhone 14 Pro")
    Text("$999")
}
```

### Accessibility Testing

**iOS Testing**:
- Enable VoiceOver (Settings > Accessibility > VoiceOver)
- Test with larger text sizes
- Check color contrast with Accessibility Inspector
- Test keyboard navigation
- Use Accessibility Inspector in Xcode

**Android Testing**:
- Enable TalkBack (Settings > Accessibility > TalkBack)
- Test with font scaling (Settings > Display > Font size)
- Check touch target sizes (Settings > Developer Options > Show layout bounds)
- Use Accessibility Scanner app
- Test with keyboard navigation

## Platform Differences Summary

### iOS vs Android Key Differences

| Aspect | iOS | Android |
|--------|-----|---------|
| **Navigation** | Bottom tab bar, navigation stack | Bottom nav, drawer, app bar |
| **Back Button** | Top-left in nav bar | Hardware/gesture back |
| **Modals** | Sheets from bottom | Dialogs center/bottom sheets |
| **Actions** | Swipe gestures, context menus | Floating action button, menus |
| **Typography** | SF Pro, text styles | Roboto, type scale |
| **Touch Target** | 44x44 pt minimum | 48x48 dp minimum |
| **Gestures** | Long press for context menu | Long press for selection |
| **Settings** | In-app settings screen | System settings + in-app |
| **Sharing** | Share sheet | Share dialog |
| **Confirmation** | Action sheets | Dialogs |

### When to Follow Platform Conventions

**Always follow**:
- Navigation patterns
- System gestures
- Text input behavior
- Permissions flow
- Notification handling

**Can customize**:
- Brand colors (within accessibility guidelines)
- Custom animations
- Content layout
- Iconography (with platform-appropriate alternatives)

## Best Practices

### Mobile UX Guidelines

1. **Touch-Friendly**:
   - Minimum 44pt/48dp touch targets
   - Adequate spacing between tappable elements
   - Visual feedback on touch (highlight, ripple)

2. **Thumb-Friendly**:
   - Important actions within thumb reach
   - Bottom navigation for frequent actions
   - Consider one-handed use

3. **Performance**:
   - Perceived performance (show loading states)
   - 60fps animations
   - Instant feedback on interactions

4. **Readable**:
   - Adequate contrast (4.5:1 minimum)
   - Support dynamic type/font scaling
   - Readable font sizes (minimum 12pt/11sp for body text)

5. **Clear Hierarchy**:
   - Visual hierarchy with size, weight, color
   - One primary action per screen
   - Progressive disclosure (show only what's needed)

6. **Forgiving**:
   - Easy undo/redo
   - Confirmation for destructive actions
   - Auto-save when possible

7. **Accessible**:
   - Screen reader support
   - Keyboard navigation
   - High contrast support
   - Color is not the only indicator

8. **Responsive**:
   - Adapt to different screen sizes
   - Support landscape orientation
   - Handle keyboard appearance

### Testing Checklist

- [ ] Test on actual devices (not just simulator)
- [ ] Test with VoiceOver/TalkBack enabled
- [ ] Test with largest text size
- [ ] Test in both light and dark mode
- [ ] Test landscape orientation
- [ ] Test on smallest supported device
- [ ] Test with slow network (offline first)
- [ ] Test gestures and touch targets
- [ ] Test keyboard navigation
- [ ] Test color contrast

## Summary

Mobile UX requires:
1. **Platform Knowledge**: Understand iOS HIG and Material Design 3
2. **Touch Optimization**: Proper touch targets, gestures, and feedback
3. **Responsive Design**: Adapt to various screen sizes and orientations
4. **Accessibility**: Support screen readers, dynamic type, and high contrast
5. **Navigation Patterns**: Use platform-appropriate navigation
6. **Performance**: Ensure smooth 60fps animations and instant feedback
7. **Consistency**: Follow platform conventions while maintaining brand

Build mobile interfaces that feel native to each platform while providing excellent user experiences for all users.
