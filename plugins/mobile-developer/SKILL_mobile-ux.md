# Mobile UX Design Skill

## Overview

This skill covers mobile-first UX patterns, iOS Human Interface Guidelines, Material Design principles, touch interactions, gestures, mobile navigation patterns, and responsive layouts for optimal mobile user experiences.

## Core Mobile UX Principles

1. **Thumb-Friendly Design**: Primary actions within thumb reach
2. **One-Handed Use**: Support common tasks with one hand
3. **Progressive Disclosure**: Show only what's needed, when needed
4. **Clear Hierarchy**: Visual hierarchy guides user attention
5. **Instant Feedback**: Immediate response to user actions
6. **Forgiving UX**: Easy undo, confirmation for destructive actions
7. **Performance**: Fast loading, smooth animations (60fps)
8. **Accessibility**: Usable by everyone, including those with disabilities

## Touch Targets & Spacing

### Minimum Touch Target Sizes

**iOS (Human Interface Guidelines)**:
- Minimum: 44 x 44 points (88 x 88 pixels @2x)
- Recommended: 48 x 48 points for primary actions
- Spacing between targets: Minimum 8 points

**Android (Material Design)**:
- Minimum: 48 x 48 dp
- Recommended: 56 x 56 dp for FABs
- Spacing between targets: Minimum 8 dp

**Cross-Platform Safe Zone**:
- Touch targets: 48 x 48 pt/dp minimum
- Spacing: 8-16 pt/dp between interactive elements
- Critical actions: 56 x 56 pt/dp or larger

### Thumb Zones

```
┌─────────────────────┐
│                     │  Hard to reach
│    ┌─────────┐      │  (requires hand shift)
│    │ NATURAL │      │
│    │  ZONE   │      │  Natural thumb zone
│    └─────────┘      │  (comfortable reach)
│                     │
│═══════════════════  │  Easy to reach
│   PRIMARY ACTIONS   │  (bottom third)
└─────────────────────┘
```

**Design implications**:
- Place primary actions in bottom third
- Navigation in top (tab bar) or bottom (bottom nav)
- Critical actions within thumb's natural reach
- Avoid placing important actions in top corners

### Spacing System

**iOS Spacing Scale** (points):
```
4pt  - Tight spacing (labels, small elements)
8pt  - Default spacing (cards, list items)
16pt - Section spacing
24pt - Large spacing (between major sections)
32pt - Extra large spacing
```

**Android Spacing Scale** (dp):
```
4dp  - Tight spacing
8dp  - Default spacing
16dp - Comfortable spacing
24dp - Large spacing
32dp - Extra large spacing
```

**Responsive Spacing**:
- Increase spacing on larger screens (tablets)
- Maintain minimum touch targets
- Use percentage-based spacing when appropriate

## Gestures

### Standard Gestures

**iOS Standard Gestures**:
- **Tap**: Select, activate
- **Double Tap**: Zoom (maps, images)
- **Long Press**: Context menu, additional options
- **Swipe Left/Right**: Navigate, reveal actions
- **Swipe Up/Down**: Scroll, refresh
- **Pinch**: Zoom in/out
- **Rotation**: Rotate content (images, maps)
- **Edge Swipe**: Back navigation (from left edge)

**Android Standard Gestures**:
- **Tap**: Select, activate
- **Long Press**: Context menu, drag & drop
- **Swipe**: Navigate, dismiss, reveal actions
- **Pull to Refresh**: Update content
- **Pinch**: Zoom
- **Edge Swipe**: Navigation drawer (from left edge)
- **Swipe Up**: Home/Recents (system gesture)

### Swipe Actions (Lists)

**iOS Swipe Pattern**:
```swift
List {
    ForEach(items) { item in
        Text(item.title)
            .swipeActions(edge: .trailing, allowsFullSwipe: true) {
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
            .swipeActions(edge: .leading) {
                Button {
                    markAsRead(item)
                } label: {
                    Label("Read", systemImage: "envelope.open")
                }
                .tint(.green)
            }
    }
}
```

**Android Swipe Pattern**:
```kotlin
@Composable
fun SwipeableListItem(
    item: Item,
    onDelete: () -> Unit,
    onArchive: () -> Unit
) {
    val swipeState = rememberSwipeToDismissState(
        confirmValueChange = { dismissValue ->
            when (dismissValue) {
                SwipeToDismissValue.StartToEnd -> {
                    onArchive()
                    true
                }
                SwipeToDismissValue.EndToStart -> {
                    onDelete()
                    true
                }
                else -> false
            }
        }
    )

    SwipeToDismiss(
        state = swipeState,
        background = {
            SwipeBackground(swipeState.targetValue)
        },
        dismissContent = {
            ListItemContent(item)
        }
    )
}
```

### Pull to Refresh

**iOS Implementation**:
```swift
ScrollView {
    content
}
.refreshable {
    await viewModel.refresh()
}
```

**Android Implementation**:
```kotlin
val pullRefreshState = rememberPullRefreshState(
    refreshing = isRefreshing,
    onRefresh = { viewModel.refresh() }
)

Box(modifier = Modifier.pullRefresh(pullRefreshState)) {
    LazyColumn {
        items(data) { item ->
            ListItem(item)
        }
    }

    PullRefreshIndicator(
        refreshing = isRefreshing,
        state = pullRefreshState,
        modifier = Modifier.align(Alignment.TopCenter)
    )
}
```

## Navigation Patterns

### Bottom Navigation (iOS/Android)

**When to use**:
- 3-5 top-level destinations
- Frequent switching between sections
- Equal importance destinations

**iOS Tab Bar**:
```swift
TabView(selection: $selectedTab) {
    HomeView()
        .tabItem {
            Label("Home", systemImage: "house")
        }
        .tag(Tab.home)

    SearchView()
        .tabItem {
            Label("Search", systemImage: "magnifyingglass")
        }
        .tag(Tab.search)

    ProfileView()
        .tabItem {
            Label("Profile", systemImage: "person")
        }
        .tag(Tab.profile)
}
```

**Android Bottom Navigation**:
```kotlin
Scaffold(
    bottomBar = {
        NavigationBar {
            NavigationBarItem(
                icon = { Icon(Icons.Default.Home, contentDescription = null) },
                label = { Text("Home") },
                selected = currentRoute == "home",
                onClick = { navController.navigate("home") }
            )
            NavigationBarItem(
                icon = { Icon(Icons.Default.Search, contentDescription = null) },
                label = { Text("Search") },
                selected = currentRoute == "search",
                onClick = { navController.navigate("search") }
            )
            NavigationBarItem(
                icon = { Icon(Icons.Default.Person, contentDescription = null) },
                label = { Text("Profile") },
                selected = currentRoute == "profile",
                onClick = { navController.navigate("profile") }
            )
        }
    }
) { paddingValues ->
    NavHost(
        navController = navController,
        startDestination = "home",
        modifier = Modifier.padding(paddingValues)
    ) {
        // Navigation graph
    }
}
```

**Best Practices**:
- Maximum 5 items
- Always show labels (don't hide on scroll)
- Use clear, recognizable icons
- Highlight selected item
- Badge for notifications (e.g., "3" on messages)

### Navigation Drawer (Android)

**When to use**:
- 6+ destinations
- Hierarchical navigation structure
- Secondary features

```kotlin
val drawerState = rememberDrawerState(DrawerValue.Closed)
val scope = rememberCoroutineScope()

ModalNavigationDrawer(
    drawerState = drawerState,
    drawerContent = {
        ModalDrawerSheet {
            Text("Menu", modifier = Modifier.padding(16.dp))
            Divider()

            NavigationDrawerItem(
                icon = { Icon(Icons.Default.Home, contentDescription = null) },
                label = { Text("Home") },
                selected = currentRoute == "home",
                onClick = {
                    scope.launch { drawerState.close() }
                    navController.navigate("home")
                }
            )

            NavigationDrawerItem(
                icon = { Icon(Icons.Default.Settings, contentDescription = null) },
                label = { Text("Settings") },
                selected = currentRoute == "settings",
                onClick = {
                    scope.launch { drawerState.close() }
                    navController.navigate("settings")
                }
            )
        }
    }
) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("App") },
                navigationIcon = {
                    IconButton(onClick = { scope.launch { drawerState.open() } }) {
                        Icon(Icons.Default.Menu, contentDescription = "Menu")
                    }
                }
            )
        }
    ) { paddingValues ->
        // Content
    }
}
```

### Modal Sheets

**iOS Sheet**:
```swift
struct ContentView: View {
    @State private var showingSheet = false

    var body: some View {
        Button("Show Sheet") {
            showingSheet = true
        }
        .sheet(isPresented: $showingSheet) {
            SheetContent()
                .presentationDetents([.medium, .large])
                .presentationDragIndicator(.visible)
        }
    }
}
```

**Android Bottom Sheet**:
```kotlin
val sheetState = rememberModalBottomSheetState()
var showBottomSheet by remember { mutableStateOf(false) }

Button(onClick = { showBottomSheet = true }) {
    Text("Show Bottom Sheet")
}

if (showBottomSheet) {
    ModalBottomSheet(
        onDismissRequest = { showBottomSheet = false },
        sheetState = sheetState
    ) {
        // Sheet content
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
        ) {
            Text("Bottom Sheet", style = MaterialTheme.typography.headlineSmall)
            Spacer(modifier = Modifier.height(16.dp))
            Text("Content goes here...")
        }
    }
}
```

### Deep Hierarchical Navigation

**iOS NavigationStack**:
```swift
NavigationStack(path: $navigationPath) {
    ProductListView()
        .navigationDestination(for: Product.self) { product in
            ProductDetailView(product: product)
        }
        .navigationDestination(for: Review.self) { review in
            ReviewDetailView(review: review)
        }
}
```

**Android Navigation**:
```kotlin
NavHost(navController = navController, startDestination = "products") {
    composable("products") {
        ProductListScreen(
            onProductClick = { productId ->
                navController.navigate("product/$productId")
            }
        )
    }

    composable(
        route = "product/{productId}",
        arguments = listOf(navArgument("productId") { type = NavType.StringType })
    ) { backStackEntry ->
        val productId = backStackEntry.arguments?.getString("productId")!!
        ProductDetailScreen(
            productId = productId,
            onReviewClick = { reviewId ->
                navController.navigate("review/$reviewId")
            },
            onBack = { navController.navigateUp() }
        )
    }

    composable("review/{reviewId}") { backStackEntry ->
        val reviewId = backStackEntry.arguments?.getString("reviewId")!!
        ReviewDetailScreen(
            reviewId = reviewId,
            onBack = { navController.navigateUp() }
        )
    }
}
```

## Mobile Layout Patterns

### Card-Based Layouts

**iOS Card**:
```swift
VStack(alignment: .leading, spacing: 8) {
    AsyncImage(url: product.imageURL) { image in
        image
            .resizable()
            .aspectRatio(contentMode: .fill)
    } placeholder: {
        Color.gray.opacity(0.2)
    }
    .frame(height: 200)
    .clipped()

    VStack(alignment: .leading, spacing: 4) {
        Text(product.name)
            .font(.headline)

        Text(product.description)
            .font(.subheadline)
            .foregroundColor(.secondary)
            .lineLimit(2)

        HStack {
            Text(product.formattedPrice)
                .font(.title3)
                .fontWeight(.bold)

            Spacer()

            Button(action: addToCart) {
                Label("Add", systemImage: "cart.badge.plus")
            }
            .buttonStyle(.bordered)
        }
    }
    .padding()
}
.background(Color(.systemBackground))
.cornerRadius(12)
.shadow(radius: 2)
```

**Android Card**:
```kotlin
Card(
    modifier = Modifier
        .fillMaxWidth()
        .padding(horizontal = 16.dp, vertical = 8.dp),
    onClick = onClick
) {
    Column {
        AsyncImage(
            model = product.imageUrl,
            contentDescription = product.name,
            modifier = Modifier
                .fillMaxWidth()
                .height(200.dp),
            contentScale = ContentScale.Crop
        )

        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            Text(
                text = product.name,
                style = MaterialTheme.typography.titleMedium
            )

            Text(
                text = product.description,
                style = MaterialTheme.typography.bodyMedium,
                maxLines = 2,
                overflow = TextOverflow.Ellipsis
            )

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = product.formattedPrice,
                    style = MaterialTheme.typography.titleLarge,
                    fontWeight = FontWeight.Bold
                )

                Button(onClick = onAddToCart) {
                    Icon(Icons.Default.ShoppingCart, contentDescription = null)
                    Spacer(modifier = Modifier.width(4.dp))
                    Text("Add")
                }
            }
        }
    }
}
```

### List Patterns

**Simple List**:
- Single line text
- Optional leading icon/image
- Optional trailing action

**Two-Line List**:
- Primary text (headline)
- Secondary text (supporting)
- Optional icon/image

**Three-Line List**:
- Title
- Subtitle
- Description
- Thumbnail/icon

**iOS List Styling**:
```swift
List {
    Section("Recent") {
        ForEach(recentItems) { item in
            HStack {
                Image(systemName: item.icon)
                    .frame(width: 32, height: 32)
                    .foregroundColor(.blue)

                VStack(alignment: .leading, spacing: 2) {
                    Text(item.title)
                        .font(.headline)

                    Text(item.subtitle)
                        .font(.caption)
                        .foregroundColor(.secondary)
                }

                Spacer()

                Text(item.time)
                    .font(.caption)
                    .foregroundColor(.secondary)

                Image(systemName: "chevron.right")
                    .foregroundColor(.secondary)
            }
        }
    }
}
.listStyle(.insetGrouped)
```

**Android List Styling**:
```kotlin
LazyColumn(
    contentPadding = PaddingValues(vertical = 8.dp)
) {
    items(items) { item ->
        ListItem(
            headlineContent = { Text(item.title) },
            supportingContent = { Text(item.subtitle) },
            leadingContent = {
                Icon(
                    item.icon,
                    contentDescription = null,
                    modifier = Modifier.size(40.dp)
                )
            },
            trailingContent = {
                Column(
                    horizontalAlignment = Alignment.End
                ) {
                    Text(
                        item.time,
                        style = MaterialTheme.typography.labelSmall
                    )
                    Icon(
                        Icons.Default.ChevronRight,
                        contentDescription = null
                    )
                }
            },
            modifier = Modifier.clickable { onItemClick(item) }
        )
    }
}
```

### Grid Layouts

**iOS Grid**:
```swift
ScrollView {
    LazyVGrid(
        columns: [
            GridItem(.adaptive(minimum: 160), spacing: 16)
        ],
        spacing: 16
    ) {
        ForEach(products) { product in
            ProductGridItem(product: product)
        }
    }
    .padding()
}

struct ProductGridItem: View {
    let product: Product

    var body: some View {
        VStack(alignment: .leading) {
            AsyncImage(url: product.imageURL) { image in
                image
                    .resizable()
                    .aspectRatio(1, contentMode: .fill)
            } placeholder: {
                Color.gray.opacity(0.2)
            }
            .frame(height: 160)
            .cornerRadius(8)

            Text(product.name)
                .font(.subheadline)
                .lineLimit(2)

            Text(product.formattedPrice)
                .font(.caption)
                .foregroundColor(.secondary)
        }
    }
}
```

**Android Grid**:
```kotlin
LazyVerticalGrid(
    columns = GridCells.Adaptive(minSize = 160.dp),
    contentPadding = PaddingValues(16.dp),
    horizontalArrangement = Arrangement.spacedBy(16.dp),
    verticalArrangement = Arrangement.spacedBy(16.dp)
) {
    items(products) { product ->
        ProductGridItem(product = product)
    }
}

@Composable
fun ProductGridItem(product: Product) {
    Column {
        AsyncImage(
            model = product.imageUrl,
            contentDescription = product.name,
            modifier = Modifier
                .fillMaxWidth()
                .aspectRatio(1f)
                .clip(RoundedCornerShape(8.dp)),
            contentScale = ContentScale.Crop
        )

        Spacer(modifier = Modifier.height(8.dp))

        Text(
            text = product.name,
            style = MaterialTheme.typography.bodyMedium,
            maxLines = 2,
            overflow = TextOverflow.Ellipsis
        )

        Text(
            text = product.formattedPrice,
            style = MaterialTheme.typography.bodySmall,
            color = MaterialTheme.colorScheme.secondary
        )
    }
}
```

## Responsive Design

### Breakpoints

**iOS Size Classes**:
- **Compact Width**: iPhone portrait, iPhone landscape (smaller models)
- **Regular Width**: iPad, iPhone landscape (Plus/Max models)
- **Compact Height**: iPhone landscape
- **Regular Height**: iPhone portrait, iPad

**Android Breakpoints** (dp):
- **Compact**: width < 600dp (phones portrait)
- **Medium**: 600dp ≤ width < 840dp (tablets portrait, phones landscape)
- **Expanded**: width ≥ 840dp (tablets landscape, desktop)

### Adaptive Layouts

**iOS Adaptive Layout**:
```swift
struct AdaptiveView: View {
    @Environment(\.horizontalSizeClass) var horizontalSizeClass

    var body: some View {
        if horizontalSizeClass == .compact {
            // Phone layout
            VStack {
                Header()
                Content()
                Footer()
            }
        } else {
            // Tablet/landscape layout
            HStack {
                Sidebar()
                VStack {
                    Header()
                    Content()
                    Footer()
                }
            }
        }
    }
}
```

**Android Adaptive Layout**:
```kotlin
@Composable
fun AdaptiveLayout() {
    val windowSizeClass = currentWindowAdaptiveInfo().windowSizeClass

    when (windowSizeClass.windowWidthSizeClass) {
        WindowWidthSizeClass.COMPACT -> {
            // Phone layout
            Column {
                Header()
                Content()
                Footer()
            }
        }

        WindowWidthSizeClass.MEDIUM,
        WindowWidthSizeClass.EXPANDED -> {
            // Tablet layout
            Row {
                NavigationRail()
                Column(modifier = Modifier.weight(1f)) {
                    Header()
                    Content()
                }
            }
        }
    }
}
```

### Safe Areas & Insets

**iOS Safe Area**:
```swift
VStack {
    content
}
.padding(.horizontal) // Respect safe area edges
.ignoresSafeArea(edges: .bottom) // Extend to bottom (e.g., for images)
```

**Android System Bars Padding**:
```kotlin
Scaffold { paddingValues ->
    LazyColumn(
        modifier = Modifier.padding(paddingValues), // Respects system bars
        contentPadding = PaddingValues(horizontal = 16.dp)
    ) {
        items(data) { item ->
            ListItem(item)
        }
    }
}
```

## Forms & Input

### Input Fields

**iOS Text Field**:
```swift
Form {
    Section("Personal Information") {
        TextField("Name", text: $name)
            .textContentType(.name)
            .autocapitalization(.words)

        TextField("Email", text: $email)
            .textContentType(.emailAddress)
            .keyboardType(.emailAddress)
            .autocapitalization(.none)

        SecureField("Password", text: $password)
            .textContentType(.newPassword)
    }

    Section {
        DatePicker("Birth Date", selection: $birthDate, displayedComponents: .date)

        Picker("Country", selection: $country) {
            ForEach(countries) { country in
                Text(country.name).tag(country)
            }
        }
    }
}
```

**Android Text Field**:
```kotlin
Column(
    modifier = Modifier
        .fillMaxWidth()
        .padding(16.dp),
    verticalArrangement = Arrangement.spacedBy(16.dp)
) {
    OutlinedTextField(
        value = name,
        onValueChange = { name = it },
        label = { Text("Name") },
        keyboardOptions = KeyboardOptions(
            capitalization = KeyboardCapitalization.Words,
            keyboardType = KeyboardType.Text
        ),
        modifier = Modifier.fillMaxWidth()
    )

    OutlinedTextField(
        value = email,
        onValueChange = { email = it },
        label = { Text("Email") },
        keyboardOptions = KeyboardOptions(
            keyboardType = KeyboardType.Email
        ),
        modifier = Modifier.fillMaxWidth()
    )

    OutlinedTextField(
        value = password,
        onValueChange = { password = it },
        label = { Text("Password") },
        visualTransformation = PasswordVisualTransformation(),
        keyboardOptions = KeyboardOptions(
            keyboardType = KeyboardType.Password
        ),
        modifier = Modifier.fillMaxWidth()
    )
}
```

### Form Validation

**Real-time Validation**:
- Validate on blur (when field loses focus)
- Show errors only after user interaction
- Provide helpful error messages
- Disable submit until form is valid

**iOS Form Validation**:
```swift
struct LoginForm: View {
    @State private var email = ""
    @State private var password = ""
    @State private var emailError: String?
    @State private var passwordError: String?

    var isFormValid: Bool {
        emailError == nil && passwordError == nil && !email.isEmpty && !password.isEmpty
    }

    var body: some View {
        Form {
            Section {
                TextField("Email", text: $email)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .autocapitalization(.none)
                    .onChange(of: email) { _, newValue in
                        validateEmail(newValue)
                    }

                if let error = emailError {
                    Text(error)
                        .font(.caption)
                        .foregroundColor(.red)
                }

                SecureField("Password", text: $password)
                    .textContentType(.password)
                    .onChange(of: password) { _, newValue in
                        validatePassword(newValue)
                    }

                if let error = passwordError {
                    Text(error)
                        .font(.caption)
                        .foregroundColor(.red)
                }
            }

            Section {
                Button("Sign In") {
                    signIn()
                }
                .disabled(!isFormValid)
            }
        }
    }

    func validateEmail(_ email: String) {
        if email.isEmpty {
            emailError = "Email is required"
        } else if !email.contains("@") {
            emailError = "Invalid email format"
        } else {
            emailError = nil
        }
    }

    func validatePassword(_ password: String) {
        if password.isEmpty {
            passwordError = "Password is required"
        } else if password.count < 8 {
            passwordError = "Password must be at least 8 characters"
        } else {
            passwordError = nil
        }
    }
}
```

## Loading & Empty States

### Loading Indicators

**iOS**:
```swift
// Inline loading
if viewModel.isLoading {
    ProgressView()
        .progressViewStyle(.circular)
}

// Full-screen loading
if viewModel.isLoading {
    VStack(spacing: 16) {
        ProgressView()
            .scaleEffect(1.5)

        Text("Loading products...")
            .font(.subheadline)
            .foregroundColor(.secondary)
    }
}

// Skeleton loading
VStack(alignment: .leading, spacing: 8) {
    RoundedRectangle(cornerRadius: 8)
        .fill(Color.gray.opacity(0.2))
        .frame(height: 200)

    RoundedRectangle(cornerRadius: 4)
        .fill(Color.gray.opacity(0.2))
        .frame(height: 20)

    RoundedRectangle(cornerRadius: 4)
        .fill(Color.gray.opacity(0.2))
        .frame(width: 100, height: 16)
}
.redacted(reason: .placeholder)
```

**Android**:
```kotlin
// Inline loading
if (isLoading) {
    CircularProgressIndicator()
}

// Full-screen loading
if (isLoading) {
    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            CircularProgressIndicator()
            Text(
                "Loading products...",
                style = MaterialTheme.typography.bodyMedium
            )
        }
    }
}

// Skeleton loading
@Composable
fun SkeletonCard() {
    Card(modifier = Modifier.fillMaxWidth()) {
        Column {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(200.dp)
                    .shimmerEffect()
            )

            Column(modifier = Modifier.padding(16.dp)) {
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(20.dp)
                        .shimmerEffect()
                )

                Spacer(modifier = Modifier.height(8.dp))

                Box(
                    modifier = Modifier
                        .fillMaxWidth(0.6f)
                        .height(16.dp)
                        .shimmerEffect()
                )
            }
        }
    }
}
```

### Empty States

**Design Principles**:
- Clear illustration or icon
- Helpful message explaining why it's empty
- Actionable CTA when possible
- Maintain brand personality

**iOS Empty State**:
```swift
ContentUnavailableView {
    Label("No Products", systemImage: "cart")
} description: {
    Text("Add products to your cart to see them here")
} actions: {
    Button("Browse Products") {
        navigateToBrowse()
    }
    .buttonStyle(.borderedProminent)
}
```

**Android Empty State**:
```kotlin
@Composable
fun EmptyState(
    title: String,
    description: String,
    icon: ImageVector,
    actionLabel: String? = null,
    onAction: (() -> Unit)? = null
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(32.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalAlignment = Arrangement.Center
    ) {
        Icon(
            imageVector = icon,
            contentDescription = null,
            modifier = Modifier.size(80.dp),
            tint = MaterialTheme.colorScheme.secondary
        )

        Spacer(modifier = Modifier.height(16.dp))

        Text(
            text = title,
            style = MaterialTheme.typography.titleLarge,
            textAlign = TextAlign.Center
        )

        Spacer(modifier = Modifier.height(8.dp))

        Text(
            text = description,
            style = MaterialTheme.typography.bodyMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            textAlign = TextAlign.Center
        )

        if (actionLabel != null && onAction != null) {
            Spacer(modifier = Modifier.height(24.dp))

            Button(onClick = onAction) {
                Text(actionLabel)
            }
        }
    }
}
```

## Error Handling

### Error Messages

**Principles**:
- Clear, user-friendly language (not technical)
- Explain what happened
- Suggest what to do next
- Provide retry action when appropriate

**iOS Error Display**:
```swift
@ViewBuilder
func errorView(message: String, retry: @escaping () -> Void) -> some View {
    ContentUnavailableView {
        Label("Error", systemImage: "exclamationmark.triangle")
    } description: {
        Text(message)
    } actions: {
        Button("Try Again") {
            retry()
        }
        .buttonStyle(.borderedProminent)
    }
}
```

**Android Error Display**:
```kotlin
@Composable
fun ErrorState(
    message: String,
    onRetry: () -> Unit,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(32.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalAlignment = Arrangement.Center
    ) {
        Icon(
            imageVector = Icons.Default.Error,
            contentDescription = null,
            modifier = Modifier.size(64.dp),
            tint = MaterialTheme.colorScheme.error
        )

        Spacer(modifier = Modifier.height(16.dp))

        Text(
            text = "Something went wrong",
            style = MaterialTheme.typography.titleMedium
        )

        Spacer(modifier = Modifier.height(8.dp))

        Text(
            text = message,
            style = MaterialTheme.typography.bodyMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            textAlign = TextAlign.Center
        )

        Spacer(modifier = Modifier.height(24.dp))

        Button(onClick = onRetry) {
            Icon(Icons.Default.Refresh, contentDescription = null)
            Spacer(modifier = Modifier.width(8.dp))
            Text("Try Again")
        }
    }
}
```

### Snackbars / Toasts

**iOS (Alert)**:
```swift
.alert("Success", isPresented: $showAlert) {
    Button("OK") { }
} message: {
    Text("Product added to cart")
}
```

**Android (Snackbar)**:
```kotlin
val snackbarHostState = remember { SnackbarHostState() }
val scope = rememberCoroutineScope()

Scaffold(
    snackbarHost = { SnackbarHost(snackbarHostState) }
) {
    // Content

    Button(onClick = {
        scope.launch {
            snackbarHostState.showSnackbar(
                message = "Product added to cart",
                actionLabel = "View Cart",
                duration = SnackbarDuration.Short
            )
        }
    }) {
        Text("Add to Cart")
    }
}
```

## Accessibility

### iOS Accessibility

```swift
Text("Product Name")
    .accessibilityLabel("Product: \(product.name)")
    .accessibilityHint("Double tap to view details")

Button(action: delete) {
    Image(systemName: "trash")
}
.accessibilityLabel("Delete")
.accessibilityHint("Deletes this item")

// Custom accessibility actions
.accessibilityElement(children: .combine)
.accessibilityActions {
    Button("Share") { share() }
    Button("Delete") { delete() }
}

// Dynamic Type support
Text("Title")
    .font(.headline)
    .dynamicTypeSize(...DynamicTypeSize.xxxLarge) // Limit max size if needed
```

### Android Accessibility

```kotlin
Text(
    text = "Product Name",
    modifier = Modifier.semantics {
        contentDescription = "Product: ${product.name}"
        stateDescription = "Tap to view details"
    }
)

IconButton(
    onClick = { delete() },
    modifier = Modifier.semantics {
        contentDescription = "Delete item"
    }
) {
    Icon(Icons.Default.Delete, contentDescription = null)
}

// Custom accessibility actions
Modifier.semantics {
    customActions = listOf(
        CustomAccessibilityAction("Share") { share(); true },
        CustomAccessibilityAction("Delete") { delete(); true }
    )
}
```

## Best Practices Summary

### Do's
- Design for thumbs (44pt/48dp minimum)
- Use standard platform patterns
- Provide immediate feedback
- Support offline usage
- Test with real users
- Follow platform guidelines
- Optimize for performance (60fps)
- Support accessibility
- Use proper spacing
- Clear visual hierarchy

### Don'ts
- Don't use tiny touch targets
- Don't hide navigation
- Don't auto-play videos with sound
- Don't use custom gestures unless necessary
- Don't ignore platform conventions
- Don't block the UI thread
- Don't forget empty states
- Don't use confusing error messages
- Don't overcomplicate navigation
- Don't ignore safe areas

### Performance UX
- First Contentful Paint < 1s
- Time to Interactive < 2s
- Smooth animations (60fps)
- Fast navigation transitions
- Optimized images (lazy loading)
- Skeleton screens while loading
- Offline support where possible
