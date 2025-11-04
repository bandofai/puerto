import React, { useState, useEffect, useCallback, useMemo } from 'react';
import styles from './ComponentName.module.css';

/**
 * Props interface with full documentation
 */
export interface ComponentNameProps {
  /**
   * Required prop description
   */
  requiredProp: string;

  /**
   * Optional prop with default value
   * @default false
   */
  optionalProp?: boolean;

  /**
   * Event handler for user action
   */
  onAction?: (data: ActionData) => void;

  /**
   * Child elements
   */
  children?: React.ReactNode;

  /**
   * Additional CSS classes
   */
  className?: string;

  /**
   * ARIA label for accessibility
   */
  ariaLabel?: string;
}

/**
 * ComponentName - Brief one-line description
 *
 * Longer description explaining what this component does,
 * when to use it, and any important considerations.
 *
 * @example
 * ```tsx
 * <ComponentName
 *   requiredProp="value"
 *   onAction={(data) => console.log(data)}
 * >
 *   Child content
 * </ComponentName>
 * ```
 */
export const ComponentName = React.forwardRef<
  HTMLDivElement,
  ComponentNameProps
>(
  (
    {
      requiredProp,
      optionalProp = false,
      onAction,
      children,
      className,
      ariaLabel,
    },
    ref
  ) => {
    // State
    const [localState, setLocalState] = useState<string>('');

    // Memoized values (expensive calculations)
    const computedValue = useMemo(() => {
      return expensiveCalculation(requiredProp);
    }, [requiredProp]);

    // Callbacks (prevent re-creating on every render)
    const handleClick = useCallback(() => {
      if (onAction) {
        onAction({ data: 'value' });
      }
    }, [onAction]);

    // Effects
    useEffect(() => {
      // Setup
      const cleanup = setupSomething();

      // Cleanup
      return () => {
        cleanup();
      };
    }, [requiredProp]);

    // Render
    return (
      <div
        ref={ref}
        className={`${styles.container} ${className || ''}`}
        role="region"
        aria-label={ariaLabel || 'Component description'}
      >
        <h2 className={styles.title}>{requiredProp}</h2>
        {optionalProp && <div className={styles.optional}>Optional content</div>}
        <button
          className={styles.button}
          onClick={handleClick}
          aria-label="Action button"
        >
          Click me
        </button>
        {children}
      </div>
    );
  }
);

ComponentName.displayName = 'ComponentName';

export default ComponentName;
