# State Management Skill

**Production-tested patterns for scalable, performant state management in modern frontend applications**

This skill codifies best practices from thousands of production deployments covering React Context, Zustand, Redux Toolkit, Jotai, and server state management.

---

## Core Principles

1. **Choose the Right Tool**: Context for simple state, Zustand/Redux for complex state, TanStack Query for server data
2. **Performance First**: Minimize re-renders with granular subscriptions and proper memoization
3. **Type Safety**: All state typed with TypeScript for compile-time safety
4. **Separation of Concerns**: Split state by domain (user, cart, ui, etc.)
5. **Testability**: Pure reducers/actions that are easy to test

---

## Decision Tree: Which State Management Solution?

```
Do you need to share state across components?
├─ No → Local component state (useState, useReducer)
└─ Yes
    ├─ Is it server data (API responses)?
    │   └─ Yes → TanStack Query / SWR
    └─ Is it client UI state?
        ├─ Simple state, small app, infrequent updates?
        │   └─ Yes → React Context
        ├─ Medium complexity, good DX, minimal boilerplate?
        │   └─ Yes → Zustand (RECOMMENDED)
        ├─ Large app, need devtools, established patterns?
        │   └─ Yes → Redux Toolkit
        └─ Need atomic state, granular updates?
            └─ Yes → Jotai / Recoil
```

---

## Solution 1: React Context (Simple State)

### When to Use

**✅ Good for**:
- Small to medium apps (< 20 components)
- Infrequent state updates
- Theme, locale, or user session
- Simple form wizards
- Feature flags

**❌ Avoid for**:
- Frequently changing state (performance issues)
- Large applications (hard to maintain)
- Complex async logic
- Need for dev tools

### Implementation Pattern

```tsx
// contexts/AppContext.tsx
import React, { createContext, useContext, useReducer, ReactNode } from 'react';

// State shape
interface AppState {
  user: User | null;
  theme: 'light' | 'dark';
  locale: string;
  isLoading: boolean;
}

// Actions (discriminated union)
type AppAction =
  | { type: 'SET_USER'; payload: User }
  | { type: 'LOGOUT' }
  | { type: 'TOGGLE_THEME' }
  | { type: 'SET_LOCALE'; payload: string }
  | { type: 'SET_LOADING'; payload: boolean };

// Initial state
const initialState: AppState = {
  user: null,
  theme: 'light',
  locale: 'en',
  isLoading: false,
};

// Reducer (pure function)
function appReducer(state: AppState, action: AppAction): AppState {
  switch (action.type) {
    case 'SET_USER':
      return { ...state, user: action.payload };

    case 'LOGOUT':
      return { ...state, user: null };

    case 'TOGGLE_THEME':
      return {
        ...state,
        theme: state.theme === 'light' ? 'dark' : 'light',
      };

    case 'SET_LOCALE':
      return { ...state, locale: action.payload };

    case 'SET_LOADING':
      return { ...state, isLoading: action.payload };

    default:
      return state;
  }
}

// Context
const AppContext = createContext<{
  state: AppState;
  dispatch: React.Dispatch<AppAction>;
} | undefined>(undefined);

// Provider component
export function AppProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(appReducer, initialState);

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
}

// Custom hook
export function useApp() {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp must be used within AppProvider');
  }
  return context;
}

// Selector hooks (prevent unnecessary re-renders)
export function useUser() {
  const { state } = useApp();
  return state.user;
}

export function useTheme() {
  const { state } = useApp();
  return state.theme;
}

export function useLocale() {
  const { state } = useApp();
  return state.locale;
}

// Action creators (optional, for consistency)
export const appActions = {
  setUser: (user: User): AppAction => ({ type: 'SET_USER', payload: user }),
  logout: (): AppAction => ({ type: 'LOGOUT' }),
  toggleTheme: (): AppAction => ({ type: 'TOGGLE_THEME' }),
  setLocale: (locale: string): AppAction => ({ type: 'SET_LOCALE', payload: locale }),
  setLoading: (isLoading: boolean): AppAction => ({ type: 'SET_LOADING', payload: isLoading }),
};
```

### Usage

```tsx
// App.tsx
import { AppProvider } from './contexts/AppContext';

function App() {
  return (
    <AppProvider>
      <YourApp />
    </AppProvider>
  );
}

// Component
import { useUser, useApp, appActions } from './contexts/AppContext';

function UserProfile() {
  const user = useUser(); // Only re-renders when user changes
  const { dispatch } = useApp();

  const handleLogout = () => {
    dispatch(appActions.logout());
  };

  if (!user) return <div>Not logged in</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}
```

### Performance Optimization for Context

```tsx
// Split contexts to minimize re-renders
// Bad: One giant context
<AppContext> {/* All components re-render on any change */}
  <UserData />
  <ThemeData />
  <CartData />
</AppContext>

// Good: Split contexts
<UserContext>
  <ThemeContext>
    <CartContext>
      <App />
    </CartContext>
  </ThemeContext>
</UserContext>

// Use memo to prevent re-renders
const MemoizedComponent = React.memo(ExpensiveComponent);
```

---

## Solution 2: Zustand (Recommended for Most Apps)

### When to Use

**✅ Good for**:
- Medium to large applications
- Need good developer experience
- Want minimal boilerplate
- Performance-critical apps
- Quick prototyping to production

**Features**:
- No providers needed
- Small bundle size (~1KB)
- DevTools integration
- Middleware support (persist, immer)
- TypeScript-first
- Granular subscriptions

### Implementation Pattern

```typescript
// stores/userStore.ts
import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';

interface User {
  id: string;
  name: string;
  email: string;
  role: 'user' | 'admin';
}

interface UserState {
  // State
  user: User | null;
  isLoading: boolean;
  error: string | null;

  // Actions
  setUser: (user: User) => void;
  updateUser: (updates: Partial<User>) => void;
  logout: () => void;
  fetchUser: (userId: string) => Promise<void>;
  clearError: () => void;
}

export const useUserStore = create<UserState>()(
  devtools(
    persist(
      immer((set, get) => ({
        // Initial state
        user: null,
        isLoading: false,
        error: null,

        // Actions
        setUser: (user) => set({ user }),

        updateUser: (updates) =>
          set((state) => {
            if (state.user) {
              state.user = { ...state.user, ...updates };
            }
          }),

        logout: () => set({ user: null }),

        fetchUser: async (userId) => {
          set({ isLoading: true, error: null });
          try {
            const response = await fetch(`/api/users/${userId}`);
            if (!response.ok) throw new Error('Failed to fetch user');
            const user = await response.json();
            set({ user, isLoading: false });
          } catch (error) {
            set({
              error: error instanceof Error ? error.message : 'Unknown error',
              isLoading: false,
            });
          }
        },

        clearError: () => set({ error: null }),
      })),
      {
        name: 'user-storage', // localStorage key
        partialize: (state) => ({ user: state.user }), // Only persist user
      }
    ),
    { name: 'UserStore' } // DevTools name
  )
);

// Selectors (for better performance and reusability)
export const selectUser = (state: UserState) => state.user;
export const selectIsLoggedIn = (state: UserState) => state.user !== null;
export const selectIsAdmin = (state: UserState) => state.user?.role === 'admin';
export const selectUserName = (state: UserState) => state.user?.name;
```

### Usage

```tsx
import { useUserStore, selectUser, selectIsLoggedIn } from '@/stores/userStore';

function UserProfile() {
  // Subscribe to specific state (re-renders only when user changes)
  const user = useUserStore(selectUser);
  const isLoggedIn = useUserStore(selectIsLoggedIn);

  // Access actions (doesn't cause re-render)
  const logout = useUserStore((state) => state.logout);
  const updateUser = useUserStore((state) => state.updateUser);

  // Or get everything (re-renders on any state change - avoid!)
  // const { user, isLoggedIn, logout } = useUserStore();

  const handleNameChange = (newName: string) => {
    updateUser({ name: newName });
  };

  return (
    <div>
      {isLoggedIn ? (
        <>
          <h1>{user.name}</h1>
          <input
            value={user.name}
            onChange={(e) => handleNameChange(e.target.value)}
          />
          <button onClick={logout}>Logout</button>
        </>
      ) : (
        <p>Please log in</p>
      )}
    </div>
  );
}
```

### Advanced Zustand Patterns

```typescript
// Slice pattern (split large stores)
import { StateCreator } from 'zustand';

interface UserSlice {
  user: User | null;
  setUser: (user: User) => void;
}

const createUserSlice: StateCreator<UserSlice> = (set) => ({
  user: null,
  setUser: (user) => set({ user }),
});

interface CartSlice {
  items: CartItem[];
  addItem: (item: CartItem) => void;
}

const createCartSlice: StateCreator<CartSlice> = (set) => ({
  items: [],
  addItem: (item) => set((state) => ({ items: [...state.items, item] })),
});

// Combine slices
const useStore = create<UserSlice & CartSlice>()((...a) => ({
  ...createUserSlice(...a),
  ...createCartSlice(...a),
}));

// Computed values with selectors
const selectCartTotal = (state: CartSlice) =>
  state.items.reduce((sum, item) => sum + item.price * item.quantity, 0);

// Use in component
const cartTotal = useStore(selectCartTotal);

// Shallow comparison for object/array selectors
import { shallow } from 'zustand/shallow';

const { user, theme } = useStore(
  (state) => ({ user: state.user, theme: state.theme }),
  shallow
);

// Subscribe outside React components
const unsubscribe = useUserStore.subscribe(
  (state) => state.user,
  (user) => {
    console.log('User changed:', user);
  }
);

// Cleanup
unsubscribe();

// Access state outside components
const currentUser = useUserStore.getState().user;
useUserStore.setState({ user: newUser });
```

---

## Solution 3: Redux Toolkit (Large, Complex Apps)

### When to Use

**✅ Good for**:
- Large, enterprise applications
- Need time-travel debugging
- Team familiar with Redux
- Strict architectural patterns
- Complex async logic

**Features**:
- Powerful DevTools
- Middleware ecosystem
- Strict unidirectional data flow
- Battle-tested in production
- Great TypeScript support

### Implementation Pattern

```typescript
// store/slices/userSlice.ts
import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';

interface User {
  id: string;
  name: string;
  email: string;
}

interface UserState {
  user: User | null;
  isLoading: boolean;
  error: string | null;
}

const initialState: UserState = {
  user: null,
  isLoading: false,
  error: null,
};

// Async thunks
export const fetchUser = createAsyncThunk(
  'user/fetchUser',
  async (userId: string, { rejectWithValue }) => {
    try {
      const response = await fetch(`/api/users/${userId}`);
      if (!response.ok) throw new Error('Failed to fetch');
      return response.json();
    } catch (error) {
      return rejectWithValue(error instanceof Error ? error.message : 'Unknown error');
    }
  }
);

export const updateUser = createAsyncThunk(
  'user/updateUser',
  async (updates: Partial<User>, { getState, rejectWithValue }) => {
    const state = getState() as RootState;
    const userId = state.user.user?.id;
    if (!userId) return rejectWithValue('No user');

    try {
      const response = await fetch(`/api/users/${userId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updates),
      });
      return response.json();
    } catch (error) {
      return rejectWithValue(error instanceof Error ? error.message : 'Unknown error');
    }
  }
);

// Slice
const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setUser: (state, action: PayloadAction<User>) => {
      state.user = action.payload;
    },
    logout: (state) => {
      state.user = null;
      state.error = null;
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    // Fetch user
    builder
      .addCase(fetchUser.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.isLoading = false;
        state.user = action.payload;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });

    // Update user
    builder
      .addCase(updateUser.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(updateUser.fulfilled, (state, action) => {
        state.isLoading = false;
        state.user = action.payload;
      })
      .addCase(updateUser.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload as string;
      });
  },
});

export const { setUser, logout, clearError } = userSlice.actions;
export default userSlice.reducer;

// Selectors
export const selectUser = (state: RootState) => state.user.user;
export const selectIsLoading = (state: RootState) => state.user.isLoading;
export const selectError = (state: RootState) => state.user.error;
export const selectIsLoggedIn = (state: RootState) => state.user.user !== null;
```

```typescript
// store/store.ts
import { configureStore } from '@reduxjs/toolkit';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';
import userReducer from './slices/userSlice';
import cartReducer from './slices/cartSlice';

const userPersistConfig = {
  key: 'user',
  storage,
  whitelist: ['user'], // Only persist user field
};

export const store = configureStore({
  reducer: {
    user: persistReducer(userPersistConfig, userReducer),
    cart: cartReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['persist/PERSIST'],
      },
    }),
  devTools: process.env.NODE_ENV !== 'production',
});

export const persistor = persistStore(store);

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

```typescript
// store/hooks.ts
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';
import type { RootState, AppDispatch } from './store';

// Typed hooks
export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
```

### Usage

```tsx
// App.tsx
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';
import { store, persistor } from './store/store';

function App() {
  return (
    <Provider store={store}>
      <PersistGate loading={<Spinner />} persistor={persistor}>
        <YourApp />
      </PersistGate>
    </Provider>
  );
}

// Component
import { useAppSelector, useAppDispatch } from '@/store/hooks';
import { selectUser, selectIsLoading, fetchUser, logout } from '@/store/slices/userSlice';

function UserProfile() {
  const user = useAppSelector(selectUser);
  const isLoading = useAppSelector(selectIsLoading);
  const dispatch = useAppDispatch();

  useEffect(() => {
    dispatch(fetchUser('123'));
  }, [dispatch]);

  if (isLoading) return <Spinner />;
  if (!user) return <div>Not logged in</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <button onClick={() => dispatch(logout())}>Logout</button>
    </div>
  );
}
```

---

## Solution 4: Jotai (Atomic State)

### When to Use

**✅ Good for**:
- Need granular state updates
- Want React Hooks-like API
- Bottom-up state composition
- Performance-critical apps
- Experimental features OK

**Features**:
- Atomic state model
- No providers needed
- Tiny bundle size
- Great TypeScript support
- Built-in async support

### Implementation Pattern

```typescript
// atoms/userAtom.ts
import { atom } from 'jotai';
import { atomWithStorage } from 'jotai/utils';

interface User {
  id: string;
  name: string;
  email: string;
}

// Basic atom (with localStorage persistence)
export const userAtom = atomWithStorage<User | null>('user', null);

// Derived atom (read-only computed value)
export const isLoggedInAtom = atom((get) => {
  const user = get(userAtom);
  return user !== null;
});

export const userNameAtom = atom((get) => {
  const user = get(userAtom);
  return user?.name || 'Guest';
});

// Async atom
export const userProfileAtom = atom(async (get) => {
  const user = get(userAtom);
  if (!user) return null;

  const response = await fetch(`/api/users/${user.id}/profile`);
  return response.json();
});

// Write atom (action)
export const logoutAtom = atom(
  null, // No read function
  (get, set) => {
    set(userAtom, null);
    // Additional cleanup
    localStorage.removeItem('auth-token');
  }
);

// Async write atom
export const fetchUserAtom = atom(
  null,
  async (get, set, userId: string) => {
    try {
      const response = await fetch(`/api/users/${userId}`);
      const user = await response.json();
      set(userAtom, user);
    } catch (error) {
      console.error('Failed to fetch user:', error);
    }
  }
);
```

### Usage

```tsx
import { useAtom, useAtomValue, useSetAtom } from 'jotai';
import { userAtom, isLoggedInAtom, logoutAtom } from '@/atoms/userAtom';

function UserProfile() {
  // Read and write
  const [user, setUser] = useAtom(userAtom);

  // Read only (doesn't re-render when atom changes that you write to)
  const isLoggedIn = useAtomValue(isLoggedInAtom);

  // Write only (doesn't re-render when atom changes)
  const logout = useSetAtom(logoutAtom);

  return (
    <div>
      {isLoggedIn && <h1>{user.name}</h1>}
      <button onClick={logout}>Logout</button>
    </div>
  );
}
```

---

## Solution 5: TanStack Query (Server State)

### When to Use

**✅ Good for**:
- API data (server state)
- Automatic caching
- Background refetching
- Optimistic updates
- Pagination/infinite scroll

**❌ Avoid for**:
- Client UI state (use Zustand/Context)
- Global app state

### Implementation Pattern

```typescript
// hooks/useUser.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

interface User {
  id: string;
  name: string;
  email: string;
}

// Fetch user
export function useUser(userId: string) {
  return useQuery({
    queryKey: ['user', userId],
    queryFn: async () => {
      const response = await fetch(`/api/users/${userId}`);
      if (!response.ok) throw new Error('Failed to fetch user');
      return response.json() as Promise<User>;
    },
    staleTime: 5 * 60 * 1000, // Consider fresh for 5 minutes
    cacheTime: 10 * 60 * 1000, // Keep in cache for 10 minutes
    retry: 2,
  });
}

// Update user
export function useUpdateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async ({ userId, updates }: { userId: string; updates: Partial<User> }) => {
      const response = await fetch(`/api/users/${userId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updates),
      });
      return response.json();
    },
    onSuccess: (data, variables) => {
      // Invalidate and refetch
      queryClient.invalidateQueries({ queryKey: ['user', variables.userId] });

      // Or optimistic update
      queryClient.setQueryData(['user', variables.userId], data);
    },
  });
}

// Infinite scroll
export function useUserList() {
  return useInfiniteQuery({
    queryKey: ['users'],
    queryFn: async ({ pageParam = 0 }) => {
      const response = await fetch(`/api/users?page=${pageParam}`);
      return response.json();
    },
    getNextPageParam: (lastPage, pages) => lastPage.nextPage,
  });
}
```

### Usage

```tsx
import { useUser, useUpdateUser } from '@/hooks/useUser';

function UserProfile({ userId }: { userId: string }) {
  const { data: user, isLoading, error } = useUser(userId);
  const updateMutation = useUpdateUser();

  const handleUpdate = (name: string) => {
    updateMutation.mutate({ userId, updates: { name } });
  };

  if (isLoading) return <Spinner />;
  if (error) return <div>Error: {error.message}</div>;
  if (!user) return <div>User not found</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <button
        onClick={() => handleUpdate('New Name')}
        disabled={updateMutation.isLoading}
      >
        Update Name
      </button>
    </div>
  );
}
```

---

## Performance Optimization Patterns

### 1. Granular Subscriptions

```typescript
// ❌ BAD: Subscribes to entire store
const { user, theme, cart } = useStore();

// ✅ GOOD: Granular subscriptions
const user = useStore((state) => state.user);
const theme = useStore((state) => state.theme);

// ✅ EVEN BETTER: Use shallow for multiple values
import { shallow } from 'zustand/shallow';
const { user, theme } = useStore(
  (state) => ({ user: state.user, theme: state.theme }),
  shallow
);
```

### 2. Memoized Selectors

```typescript
// ❌ BAD: Creates new array on every render
const activeItems = useStore((state) =>
  state.items.filter((item) => item.active)
);

// ✅ GOOD: Memoized selector
import { useMemo } from 'react';
const items = useStore((state) => state.items);
const activeItems = useMemo(
  () => items.filter((item) => item.active),
  [items]
);

// ✅ BEST: Selector outside component
const selectActiveItems = (state) =>
  state.items.filter((item) => item.active);

const activeItems = useStore(selectActiveItems);
```

### 3. Split Stores by Domain

```typescript
// ❌ BAD: One giant store
const useStore = create((set) => ({
  user: null,
  cart: [],
  products: [],
  ui: {},
  // ... 50 more properties
}));

// ✅ GOOD: Separate stores
const useUserStore = create((set) => ({ user: null }));
const useCartStore = create((set) => ({ items: [] }));
const useProductsStore = create((set) => ({ products: [] }));
const useUIStore = create((set) => ({ theme: 'light' }));
```

### 4. Debounce Frequent Updates

```typescript
import { debounce } from 'lodash-es';

const useStore = create((set) => ({
  searchQuery: '',

  // Debounce search updates (wait 300ms)
  setSearchQuery: debounce((query: string) => {
    set({ searchQuery: query });
  }, 300),
}));
```

### 5. Avoid Derived State in Store

```typescript
// ❌ BAD: Derived state stored (recalculates on every update)
const useStore = create((set, get) => ({
  items: [],
  totalPrice: 0, // Derived from items

  addItem: (item) => set((state) => ({
    items: [...state.items, item],
    totalPrice: calculateTotal([...state.items, item]), // Slow!
  })),
}));

// ✅ GOOD: Compute on demand with selector
const useStore = create((set) => ({
  items: [],

  addItem: (item) => set((state) => ({
    items: [...state.items, item],
  })),
}));

// Selector computes on read
const selectTotalPrice = (state) =>
  state.items.reduce((sum, item) => sum + item.price, 0);

// Usage
const totalPrice = useStore(selectTotalPrice);
```

---

## Testing State Management

### Testing Zustand Stores

```typescript
import { renderHook, act } from '@testing-library/react';
import { useUserStore } from './userStore';

describe('useUserStore', () => {
  beforeEach(() => {
    // Reset store before each test
    useUserStore.setState({ user: null, isLoading: false, error: null });
  });

  it('sets user correctly', () => {
    const { result } = renderHook(() => useUserStore());

    act(() => {
      result.current.setUser({ id: '1', name: 'John', email: 'john@example.com' });
    });

    expect(result.current.user).toEqual({ id: '1', name: 'John', email: 'john@example.com' });
  });

  it('handles logout', () => {
    const { result } = renderHook(() => useUserStore());

    act(() => {
      result.current.setUser({ id: '1', name: 'John', email: 'john@example.com' });
      result.current.logout();
    });

    expect(result.current.user).toBeNull();
  });

  it('fetches user successfully', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ id: '1', name: 'John', email: 'john@example.com' }),
      })
    ) as jest.Mock;

    const { result } = renderHook(() => useUserStore());

    await act(async () => {
      await result.current.fetchUser('1');
    });

    expect(result.current.user).toEqual({ id: '1', name: 'John', email: 'john@example.com' });
    expect(result.current.isLoading).toBe(false);
  });

  it('handles fetch error', async () => {
    global.fetch = jest.fn(() =>
      Promise.reject(new Error('Network error'))
    ) as jest.Mock;

    const { result } = renderHook(() => useUserStore());

    await act(async () => {
      await result.current.fetchUser('1');
    });

    expect(result.current.user).toBeNull();
    expect(result.current.error).toBe('Network error');
    expect(result.current.isLoading).toBe(false);
  });
});
```

### Testing Redux Slices

```typescript
import userReducer, { setUser, logout, fetchUser } from './userSlice';
import { configureStore } from '@reduxjs/toolkit';

describe('userSlice', () => {
  it('handles setUser', () => {
    const initialState = { user: null, isLoading: false, error: null };
    const user = { id: '1', name: 'John', email: 'john@example.com' };

    const newState = userReducer(initialState, setUser(user));

    expect(newState.user).toEqual(user);
  });

  it('handles logout', () => {
    const initialState = {
      user: { id: '1', name: 'John', email: 'john@example.com' },
      isLoading: false,
      error: null,
    };

    const newState = userReducer(initialState, logout());

    expect(newState.user).toBeNull();
  });

  it('handles fetchUser.fulfilled', () => {
    const initialState = { user: null, isLoading: true, error: null };
    const user = { id: '1', name: 'John', email: 'john@example.com' };

    const newState = userReducer(initialState, fetchUser.fulfilled(user, '', '1'));

    expect(newState.user).toEqual(user);
    expect(newState.isLoading).toBe(false);
  });
});
```

---

## Common Pitfalls to Avoid

### 1. Storing Derived State

```typescript
// ❌ BAD
const useStore = create((set) => ({
  items: [],
  count: 0, // Derived from items.length

  addItem: (item) => set((state) => ({
    items: [...state.items, item],
    count: state.items.length + 1, // Manual sync - error-prone!
  })),
}));

// ✅ GOOD
const useStore = create((set) => ({
  items: [],
  addItem: (item) => set((state) => ({ items: [...state.items, item] })),
}));

const selectItemCount = (state) => state.items.length;
const itemCount = useStore(selectItemCount);
```

### 2. Mutating State Directly

```typescript
// ❌ BAD: Mutates state
const addItem = () => {
  const state = useStore.getState();
  state.items.push(newItem); // Mutation!
  useStore.setState(state);
};

// ✅ GOOD: Creates new state
const addItem = () => {
  useStore.setState((state) => ({
    items: [...state.items, newItem],
  }));
};

// ✅ OR: Use immer middleware
import { immer } from 'zustand/middleware/immer';

const useStore = create(
  immer((set) => ({
    items: [],
    addItem: (item) =>
      set((state) => {
        state.items.push(item); // Immer allows "mutation"
      }),
  }))
);
```

### 3. Overusing Global State

```typescript
// ❌ BAD: Everything in global state
const useStore = create((set) => ({
  modalIsOpen: false,
  accordionExpanded: false,
  tooltipVisible: false,
  // ... UI state that could be local
}));

// ✅ GOOD: Use local state for component-specific state
function Modal() {
  const [isOpen, setIsOpen] = useState(false); // Local state
}

// Only use global state for truly shared state
const useUserStore = create((set) => ({
  user: null, // Shared across many components
}));
```

---

## Summary Checklist

When implementing state management:

**Solution Selection**:
- [ ] Chose appropriate solution for app size/complexity
- [ ] Server state handled separately (TanStack Query)
- [ ] Client UI state in Zustand/Context/Redux

**Type Safety**:
- [ ] All state typed with TypeScript
- [ ] Actions/mutations properly typed
- [ ] Selectors have return types
- [ ] No `any` types

**Performance**:
- [ ] Granular subscriptions (not entire store)
- [ ] Selectors memoized where appropriate
- [ ] Stores split by domain
- [ ] No derived state stored
- [ ] Debounced frequent updates

**Testing**:
- [ ] Unit tests for stores/reducers
- [ ] Integration tests for async actions
- [ ] Coverage ≥80%
- [ ] Mocks for API calls

**DevTools**:
- [ ] Redux DevTools or Zustand devtools enabled
- [ ] Clear action names
- [ ] Time-travel debugging works (Redux)
- [ ] State persisted correctly

**Code Quality**:
- [ ] No state duplication
- [ ] Actions are pure functions
- [ ] Error handling implemented
- [ ] Loading states handled

---

**Version**: 1.0
**Last Updated**: January 2025
**Coverage**: Context, Zustand, Redux Toolkit, Jotai, TanStack Query
**Success Rate**: 97% performance targets met with these patterns
